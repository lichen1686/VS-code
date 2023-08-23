import requests
from bs4 import BeautifulSoup

def get_python_news_titles():
    # 请求Python官方网站的新闻页面
    url = 'https://www.python.org/blogs/'
    response = requests.get(url)
    response.raise_for_status()

    # 使用BeautifulSoup解析页面内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有新闻标题
    title_elements = soup.select('h3 a')

    # 获取标题文本
    titles = [title_element.get_text() for title_element in title_elements]

    return titles

if __name__ == '__main__':
    news_titles = get_python_news_titles()
    for idx, title in enumerate(news_titles, 1):
        print(f"{idx}. {title}")

