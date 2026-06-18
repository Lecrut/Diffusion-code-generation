from typing import Dict
class FavoriteAnimalStore:
    def __init__(self) -> None:
        self._store: Dict[str, str] = {}
    def add(self, animal_name: str) -> bool:
        normalized_key = animal_name.lower().strip()
        if not normalized_key or not isinstance(animal_name, str):
            return False
        original_entry = self._get_animal(normalized_key)
        if original_entry is None:
            self._store[normalized_key] = animal_name.strip()
            return True
        existing_value = self._store.get(normalized_key)
        if not isinstance(existing_value, str):
            return False
        if original_entry != animal_name:
            self._store[normalized_key] = animal_name.strip()
    def get(self, animal_name: str) -> bool:
        normalized_key = animal_name.lower().strip()
        if not normalized_key or not isinstance(animal_name, str):
            return False
        stored_value = self._get_animal(normalized_key)
        if stored_value is None:
            return False
        original_entry = self._store.get(normalized_key)
        return isinstance(original_entry, str) and original_entry == animal_name
    def _get_animal(self, normalized_key: str) -> bool | None:
        if not isinstance(normalized_key, str):
            raise TypeError("Key must be a string")
        return self._store.get(normalized_key.lower().strip())
    def contains(self, animal_name: str) -> bool:
        normalized = animal_name.lower().strip()
        return normalized in self._store
if __name__ == '__main__':
    store = FavoriteAnimalStore()
    test_names = ["Lion", "lEON", "lion", "Tiger"]
    print("Adding animals...")
    added_count = 0
    for name in test_names:
        if store.add(name):
            added_count += 1
    query_name = "Lion"
    is_present = store.contains(query_name)
    print(f"\nTest Results:")
    print(f"Added {added_count} animals.")
    print(f"Contains '{query_name}'? {is_present}")