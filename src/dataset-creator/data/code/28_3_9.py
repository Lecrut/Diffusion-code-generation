import json
from functools import lru_cache
@lru_cache(maxsize=None)
def get_popular_animals():
    mock_data = [
        {"name": "Lion", "scientific_name": "Panthera leo"},
        {"name": "Tiger", "scientific_name": "Panthera tigris"},
        {"name": "Elephant", "scientific_name": "Loxodonta africana"}
    ]
    return mock_data
if __name__ == '__main__':
    animals = get_popular_animals()
    for animal in animals:
        print(f"{animal['name']} ({animal['scientific_name']})")