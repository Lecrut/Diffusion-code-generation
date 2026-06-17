import functools
import json
def fetch_animals():
    return [
        {"id": 1, "name": "Lion", "category": "Mammal"},
        {"id": 2, "name": "Tiger", "category": "Mammal"},
        {"id": 3, "name": "Elephant", "category": "Mammal"}
    ]
@functools.lru_cache(maxsize=1)
def get_popular_animals():
    return fetch_animals()
if __name__ == '__main__':
    animals = get_popular_animals()
    print(json.dumps(animals, indent=2))