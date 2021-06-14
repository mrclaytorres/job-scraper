from bs4 import BeautifulSoup
import requests
import time

print(f"What job are you looking for?")
job_keyword = input('>')
print(f"Put a skill that you are not familiar with")
unfamiliar_skill = input('>')
print(f"Filtering out unfamiliar skill...")

def find_jobs():
    page_to_scrape = ('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={}&txtLocation=').format(job_keyword)
    html_text = requests.get(page_to_scrape).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for job in jobs:
        published_date = job.find('span', class_ = 'sim-posted').span.text
        
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            # more_info = job.find('a')['href']
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                #Use these lines here if you opt to save the jobs into text files inside a folder named 'posts' instead of just printing in the console.
                # with open(f"posts/{index}.txt", "w") as f:
                    # f.write(f"Company Name: {company_name.strip()} \n")
                    # f.write(f"Required Skills: {skills.strip()} \n")
                    # f.write(f"More Info: {more_info}")
                # print(f"File saved: {index}.txt")

                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"More Info: {more_info}")
                print('')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting for {time_wait} minutes...")
        time.sleep(time_wait * 60)