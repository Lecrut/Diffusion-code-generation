import json
from functools import lru_cache
@lru_cache(maxsize=128)
def fetch_animals():
    mock_data = {
        "animals": [
            {"name": "Lion", "category": "Mammal"},
            {"name": "Elephant", "category": "Mammal"},
            {"name": "Shark", "category": "Fish"}
        ]
    }
    return json.dumps(mock_data)
def main():
    try:
        result = fetch_animals()
        data = json.loads(result)
        for animal in data["animals"]:
            print(f"{animal['name']}: {animal['category']}")
    except Exception as e:
        pass
if __name__ == '__main__':
    main()