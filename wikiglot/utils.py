import requests
from bs4 import BeautifulSoup


def _get_soup(word: str, url: str) -> BeautifulSoup | None:
    params = {
        "action": "parse",
        "page": word.replace(" ", "_"),
        "format": "json",
        "prop": "text",
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        msg = f"API error for word: {word}"
        raise Exception(msg)

    data = response.json()

    if "error" in data:
        return None

    html = data["parse"]["text"]["*"]

    return BeautifulSoup(html, "html.parser")
