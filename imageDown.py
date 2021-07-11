#!/usr/bin/python3.9

import requests, os, bs4

# gets what to search for
searchName = input('\nWhat image would you like to search for? \n \n')

# url for images
url = 'https://imgur.com/search?q='

# makes folder for the images
os.makedirs(f'{searchName} images', exist_ok=True)

# gets webpage with images
res = requests.get(f'{url}+{searchName}')
res.raise_for_status()

# makes into html readable
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# holds top 5 imgs links
topImgs = []

# finds all imgs i=with the search
for img in soup.find_all('a', {'class': "image-list-link"}) :
    # gets top 5 imgs
    if len(topImgs) < 5:
        # img source
        source = img.contents[1].get('src')
        # puts img source in the list
        topImgs.append(source)
        imgUrl = 'https:'+ source
        # gets imgurl
        res = requests.get(imgUrl)
        res.raise_for_status()

        # creates imgfile
        imageFile = open(os.path.join(f'{searchName} images', os.path.basename(imgUrl)), 'wb')

        # prints adding file info
        print(f'Adding {source} to the {searchName} images folder.')
        # writes info into imagefile
        for chunk in res.iter_content(100000) :
            imageFile.write(chunk)
        # closes file
        imageFile.close
        # if the img list is 5 stop for loop
    elif len(topImgs) == 5 :
        break

print('Done')






