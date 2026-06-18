import functools
import json
from typing import List
class AnimalAPI:
    def get_popular_animals(self) -> List[dict]:
        return [
            {"name": "Lion", "population": 20500},
            {"name": "Tiger", "population": 6800},
            {"name": "Elephant", "population": 415000}
        ]
@functools.lru_cache(maxsize=1)
def fetch_animal_data() -> List[dict]:
    api = AnimalAPI()
    return json.loads(json.dumps(api.get_popular_animals()))
if __name__ == '__main__':
    data = fetch_animal_data()
    for animal in data:
        print(f"{animal['name']}: {animal['population']}")