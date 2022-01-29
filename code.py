from bs4 import BeautifulSoup
import time
import csv
START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("/Users/brianhoang/Desktop/WebScrapping/chromedriver")
browser.get(START_URL)
time.sleep(10)
headers=[
    "name",
    "distance",
    "mass",
    "radius"
]
stars=[]
def scrape():
    for i in range(0,97):
        while True:
            time.sleep(2)
            soup=BeautifulSoup(browser.page_source,"html.parser")
            current_page_num=int(soup.find_all("input",attrs={"class","page_num"})[0].get("value"))
            if current_page_num<i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif current_page_num>i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break
        for th_tag in soup.find_all("th",attrs={"name","distance",
    "mass",
    "radius"}):
            li_tags=th_tag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li_tag=li_tags[0]
            temp_list.append("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"+hyperlink_li_tag.find_all("a",href=True)[0]["href"])
            stars.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        print(f"{i}pagedone1")
