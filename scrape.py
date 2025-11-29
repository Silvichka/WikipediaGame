from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_links(title: str, lang: str = "en"):
    url_title = title.replace(" ", "_")
    url = f"https://{lang}.wikipedia.org/wiki/{url_title}"

    headers = {
        "User-Agent": f"MyWikiScraper/1.0 ({os.getenv('EMAIL')})"
    }

    print(f"Starting scrapping page: {url}\n")

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")

    links = set()

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if not href.startswith("/wiki/"):
            continue

        page_name = href[len("/wiki/"):]

        if ":" in page_name:
            continue

        links.add(page_name)

    return links

if __name__ == '__main__':
    title = "Jos%C3%A9_P%C3%A9kerman"
    r = get_links(title)
    print(len(r))
    for l in r:
        print(l)
