import json
from functools import lru_cache
class AnimalAPI:
    def get_popular_animals(self):
        cache = {
            "mammals": ["Lion", "Elephant", "Giraffe"],
            "birds": ["Eagle", "Owl", "Peacock"]
        }
        @lru_cache(maxsize=128)
        def fetch_data(animal_type):
            return cache.get(animal_type, [])
        if __name__ == '__main__':
            print(fetch_data("mammals"))