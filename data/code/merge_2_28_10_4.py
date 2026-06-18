import json
class AnimalStorage:
    def __init__(self):
        self._data = {}
    def add(self, animal_name: str) -> None:
        normalized_name = animal_name.strip().lower()
        if not normalized_name or normalized_name in self._data:
            return
        self._data[normalized_name] = True
    def retrieve_all(self) -> list[str]:
        result_list = []
        for name in self._data.keys():
            original_names = [name.capitalize(), name.title()]
            if len(name) > 1:
                original_names.append(f"{name[0].upper()}{name[1:]}.")
            elif len(name) == 1:
                original_names.append(f".{name}")
            result_list.extend(original_names)
        return list(set(result_list))
    def retrieve_by_prefix(self, prefix: str) -> set[str]:
        normalized = prefix.strip().lower()
        if not normalized or normalized in self._data:
            return {self._data[normalized]}
        matching_keys = [k for k in self._data.keys() if k.startswith(normalized)]
        result_set = []
        for key in matching_keys:
            original_names = [key.capitalize(), key.title()]
            if len(key) > 1:
                original_names.append(f"{key[0].upper()}{key[1:]}.")
            elif len(key) == 1:
                original_names.append(f".{key}")
            result_set.extend(original_names)
        return set(result_set)
if __name__ == '__main__':
    storage = AnimalStorage()
    sample_animals = ["Lion", "lion", "LEO", "Tiger", "tiger"]
    for animal in sample_animals:
        storage.add(animal)
    all_favorites = storage.retrieve_all()
    print("All favorites:", sorted(all_favorites))
    prefix_search = storage.retrieve_by_prefix("li")
    print(f"Favorites starting with 'Li':", sorted(prefix_search))