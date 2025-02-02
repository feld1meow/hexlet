import requests
from bs4 import BeautifulSoup


url = 'https://ru.hexlet.io/courses/python-setup-environment'

headers = {
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0)',
}


session = requests.session()
response = session.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')


i = 1

for element in soup.find_all(class_='row my-2'):
    name = element.find(class_="text-decoration-none text-body me-2").text.strip()
    description = element.find(class_="mt-3 text-body-secondary").text.strip()
    print(f'{i}. {name} - {description}')
    i += 1
