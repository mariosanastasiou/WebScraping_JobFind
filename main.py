from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text = requests.get('https://www.jobfind.gr/JobAds/all/all/GR/Theseis_Ergasias?cnt=1&st=%ce%97%ce%bb%ce%b5%ce%ba%cf%84%cf%81%ce%bf%ce%bb%cf%8c%ce%b3%ce%bf%cf%82%20%ce%9c%ce%b7%cf%87%ce%b1%ce%bd%ce%b9%ce%ba%cf%8c%cf%82').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_= 'jobitem')

    for index, job in enumerate(jobs) :
        c_name = job.find('h3', class_ = 'title').text
        location = soup.find('div', class_ = 'city').text
        more_info = job.find('h3', class_ = 'title').a['href']

        with open(f'posts/{index}.txt', 'w') as f:

            f.write(f"Company Name: {c_name.strip()}\n")
            f.write(f"Location: {location.strip()}\n")
            f.write(f"More Info: https://www.jobfind.gr{more_info}\n")
        print(f'File Saved : {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} mins...')
        time.sleep(time_wait * 60)         # every 10 min 