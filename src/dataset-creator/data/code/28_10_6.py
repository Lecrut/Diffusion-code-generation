import re
class FavoriteAnimalStore:
    def __init__(self):
        self._lookup = {}                                                                        
    def add(self, animal_name: str) -> None:
        normalized_key = re.sub(r'\W', '', animal_name.lower())
        if not self._lookup.get(normalized_key):
            self._lookup[normalized_key] = True
    def retrieve(self, animal_name: str) -> bool | None:
        normalized_key = re.sub(r'\W', '', animal_name.lower())
        return self._lookup.get(normalized_key)
if __name__ == '__main__':
    store = FavoriteAnimalStore()
    test_animals = ["Lion", "lion", "TIGER", "tiger"]
    print("Adding animals:", ", ".join(test_animals))
    for animal in test_animals:
        store.add(animal)
    query_cases = [
        ("lION", True),
        ("Lion", True),
        ("tiger", False),                                                                                                                            
        ("tiger", True),                                                                       
    ]
    print("\nRetrieval results:")
    for query, expected in query_cases:
        result = store.retrieve(query)
        status = "PASS" if (result is not None) == expected else f"FAIL (Expected {expected}, got {result})"
        print(f"{query}: {status}")