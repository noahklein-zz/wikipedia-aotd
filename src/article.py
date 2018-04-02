from requests_html import HTMLSession

AOTD_URL = "http://toolserver.org/~erwin85/randomarticle.php?categories=Featured_articles&family=wikipedia&lang=en"
session = HTMLSession()


def get_title(html):
    return html.find('h1', first=True).text


def get_definition(html):
    return html.find('p', first=True).html


def get_img(html):
    img = html.find('img', first=True)
    if img:
        return img.attrs.get('src')


def fetch(url=AOTD_URL):
    res = session.get(url)
    res.raise_for_status()
    html = res.html

    return {
        "url": res.url,
        "title": get_title(html),
        "defintion":  get_definition(html),
        "img": get_img(html)
    }


# print(fetch())
