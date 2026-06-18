import sys
class FavoriteAnimalStore:
    def __init__(self):
        self._store = {}                                                    
    def add(self, animal_name: str) -> None:
        normalized_key = animal_name.lower().strip()
        if not normalized_key or self._store.get(normalized_key):
            return
        entry = {
            'name': animal_name,
            'original_case': True                                 
        }
        self._store[normalized_key] = [entry]
    def get(self, search_term: str) -> list | None:
        normalized_search = search_term.lower().strip()
        if not normalized_search or normalized_search not in self._store:
            return []
        results = []
        for entry in self._store[normalized_search]:
            if 'original_case' in entry and entry['original_case']:
                results.append(entry)
            return [entry]
    def list_all(self) -> list:
        result = []
        for name, entries in self._store.items():
            if not entries or 'original_case' not in entries[0]:
                continue
            preferred_entry = next((e for e in entries if e.get('original_case')), None)
            result.append(preferred_entry['name'] if preferred_entry else name.lower())
        return sorted(result, key=lambda x: (x != x[0], x))
def main():
    store = FavoriteAnimalStore()
    samples = [
        "Lion",
        "lion",
        "  LEOPARD  ",
        "Tiger",
        "tiger"
    ]
    for animal in samples:
        store.add(animal)
    test_queries = ["LEONID", "Lion", "", None]
    print("Stored animals:")
    all_animals = store.list_all()
    if not isinstance(all_animals, list):
        all_animals = [all_animals]
    for animal in sorted(set(str(a) for a in all_animals)):
        print(f"  - {animal}")
    try:
        query_result = store.get("invalid_query")
        if not isinstance(query_result, list):
            query_result = [query_result]
        print("\nQuery results:")
        for animal in query_result:
            print(f"  - {animal}")
    except Exception as e:
        pass
if __name__ == '__main__':
    main()