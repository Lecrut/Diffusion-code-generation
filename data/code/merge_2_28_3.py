import functools
import json
from typing import List
class AnimalAPI:
    def get_popular_animals(self) -> List[dict]:
        sample_data = [
            {"name": "Lion", "population_millions": 20.6},
            {"name": "Tiger", "population_millions": 7.5},
            {"name": "Elephant", "population_millions": 415.8}
        ]
        return sample_data
@functools.lru_cache(maxsize=1)
def fetch_animal_list() -> List[dict]:
    api = AnimalAPI()
    data = api.get_popular_animals()
    return data
if __name__ == '__main__':
    animals = fetch_animal_list()
    print(json.dumps(animals))