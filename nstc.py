import requests, time
from bs4 import BeautifulSoup

target = "https://www.nstc.gov.tw/folksonomy/list/ba3d22f3-96fd-4adf-a078-91a05b8f0166?pageNum={}&view_mode=listView&l=ch"
sel = "#templateJ > div.news_list.marb_30 > a"
fp = open("nstc-recruitment.txt", "w", encoding="utf-8")
for page in range(1, 21):
    url = target.format(page)
    html = requests.get(url, verify=False).text
    soup = BeautifulSoup(html, "lxml")
    items = soup.select(sel)
    for item in items:
        try:
            fp.write(item.find(class_="date").text+"\n")
            fp.write(item.h3.text.strip()+"\n")
            if "http" not in item["href"]:
                fp.write("https://www.nstc.gov.tw" + item["href"]+"\n\n")
            else:
                fp.write(item["href"]+"\n\n")
        except:
            pass
        print(item.h3.text.strip())
    time.sleep(3)
fp.close()