import json
from functools import lru_cache
@lru_cache(maxsize=None)
def fetch_animals():
    mock_data = [
        {"name": "Lion", "category": "Mammal"},
        {"name": "Elephant", "category": "Mammal"},
        {"name": "Tiger", "category": "Mammal"},
        {"name": "Shark", "category": "Fish"},
        {"name": "Owl", "category": "Bird"}
    ]
    return mock_data
if __name__ == '__main__':
    animals = fetch_animals()
    for animal in animals:
        print(f"{animal['name']} ({animal['category']})")