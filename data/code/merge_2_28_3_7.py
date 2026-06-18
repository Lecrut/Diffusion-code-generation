import json
from functools import lru_cache
@lru_cache(maxsize=128)
def fetch_animals():
    mock_data = [
        {"name": "Lion", "category": "Mammal"},
        {"name": "Eagle", "category": "Bird"},
        {"name": "Shark", "category": "Fish"}
    ]
    return json.dumps(mock_data)
if __name__ == '__main__':
    result = fetch_animals()
    print(json.loads(result))