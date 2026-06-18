import sys
class FavoriteAnimalStore:
    def __init__(self):
        self._lookup = {}                                                                  
    def add(self, animal_name: str) -> None:
        normalized = animal_name.lower()
        if not isinstance(animal_name, str):
            raise TypeError("Animal name must be a string.")
        original_uppercase = animal_name.upper()
        self._lookup[normalized] = original_uppercase
    def get(self, search_term: str) -> str | None:
        normalized_search = search_term.lower()
        if not isinstance(search_term, str):
            raise TypeError("Search term must be a string.")
        return self._lookup.get(normalized_search)
if __name__ == '__main__':
    store = FavoriteAnimalStore()
    sample_data = [
        "Lion",
        "Tiger",
        "Eagle",
        "lion",                                                                                          
        "LEOPARD"
    ]
    for animal in sample_data:
        store.add(animal)
    test_queries = ["tiger", "TIGER", "eagle"]
    results = []
    for query in test_queries:
        result = store.get(query)
        if result is not None:
            print(f"Found '{query}': {result}")
        else:
            print(f"Not found: '{query}'")