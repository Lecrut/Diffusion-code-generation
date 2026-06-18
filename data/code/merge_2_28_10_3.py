import hashlib
class FavoriteAnimalStore:
    def __init__(self):
        self._lookup = {}
    def add(self, animal_name: str) -> None:
        normalized_key = animal_name.lower().strip()
        hash_value = hashlib.md5(normalized_key.encode()).hexdigest()[:8]
        if not isinstance(animal_name, str):
            raise TypeError("Animal name must be a string")
        self._lookup[hash_value] = {
            'original': animal_name,
            'normalized': normalized_key
        }
    def get(self, input_name: str) -> str | None:
        if not isinstance(input_name, str):
            raise TypeError("Input name must be a string")
        try:
            hash_value = hashlib.md5(input_name.lower().strip().encode()).hexdigest()[:8]
            entry = self._lookup.get(hash_value)
            return entry['original'] if entry else None
        except Exception as e:
            raise ValueError(f"Error retrieving animal name: {e}")
if __name__ == '__main__':
    store = FavoriteAnimalStore()
    sample_data = [
        "Lion",
        "lion",
        "TIGER",
        "  tiger ",
        "elephant",
        "ELEPHANT"
    ]
    for animal in sample_data:
        store.add(animal)
    test_queries = ["tiger", " Lion ", "Elephant"]
    print("Favorite Animals:")
    for query in test_queries:
        result = store.get(query)
        if result is not None:
            print(f"Query '{query}' -> {result}")
        else:
            print(f"Query '{query}' -> Not found")