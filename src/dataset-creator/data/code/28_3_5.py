import functools
import json
class AnimalAPI:
    def fetch_animals(self):
        return [
            {"name": "Lion", "category": "Mammal"},
            {"name": "Elephant", "category": "Mammal"},
            {"name": "Tiger", "category": "Mammal"}
        ]
@functools.lru_cache(maxsize=128)
def get_popular_animals():
    api = AnimalAPI()
    data = api.fetch_animals()
    return json.dumps(data)
if __name__ == '__main__':
    result = get_popular_animals()
    print(result)