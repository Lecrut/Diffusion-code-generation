import functools
import json
from typing import List
class AnimalAPI:
    def get_popular_animals(self) -> List[dict]:
        sample_data = [
            {"name": "Lion", "population_millions": 20.6},
            {"name": "Horse", "population_millions": 70},
            {"name": "Dog", "population_millions": 458},
            {"name": "Cat", "population_millions": 319}
        ]
        return sample_data
@functools.lru_cache(maxsize=2)
def fetch_animal_list() -> List[dict]:
    api = AnimalAPI()
    result = api.get_popular_animals()
    return json.dumps(result).encode('utf-8')
if __name__ == '__main__':
    cached_data = fetch_animal_list()
    print(cached_data.decode('utf-8'))