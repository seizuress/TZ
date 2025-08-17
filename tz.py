import requests

def fetch_data(url: str) -> dict:
    # GET-запрос по указанному юрл и возвращает распарсенный JSON.
    try:
        response = requests.get(url)
        response.raise_for_status()  # выбрасывает исключение при ошибке HTTP
        return response.json()
    except requests.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return {}

def parse(response: dict) -> list[str]:
    """
  должно извлекать список логинов
  list comprehension для компактности
    """
    return [
        person.get('login')
        for person in response.get('people', {}).get('result', [])
        if person.get('login') is not None
    ]
url = 'https://search.yandex-team.ru/suggest/?text=Саптех&version=2&people.per_page=10'

data = fetch_data(url)

logins = parse(data)

print("Найденные логины:", logins)