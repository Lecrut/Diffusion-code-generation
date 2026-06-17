import sys
class FavoriteAnimalStore:
    def __init__(self):
        self._lookup = {}                                                    
    def add(self, animal_name: str) -> None:
        normalized_key = animal_name.lower().strip()
        if not normalized_key or self._lookup.get(normalized_key):
            return
        self._lookup[normalized_key] = animal_name
    def get(self, query: str) -> str | None:
        normalized_query = query.lower().strip()
        if not normalized_query or len(normalized_query) > 100:
            return None
        return self._lookup.get(normalized_query, "No match found")
def main():
    store = FavoriteAnimalStore()
    test_animals = ["Lion", "Tiger", "LEOPARD", "lion"]
    queries = [
        "tiger",
        "  LEONARDO DA Vinci's favorite animal: lion ",
        "cat",
        ""
    ]
    for animal in test_animals:
        store.add(animal)
    print("Stored animals:", list(store._lookup.keys()))
    results = []
    for query in queries:
        result = store.get(query)
        if result == "No match found":
            status = "(not stored)"
        else:
            status = f"(original form: {result})"
        print(f"Query '{query}' -> {status}")
if __name__ == '__main__':
    main()