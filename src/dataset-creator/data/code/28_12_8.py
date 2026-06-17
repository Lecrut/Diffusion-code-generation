from typing import List, Dict
class FavoriteAnimalManager:
    def __init__(self) -> None:
        self._favorites_set: set[str] = set()
        self._lookup_dict: dict[str, int] = {}
    def add_favorite(self, animal_name: str) -> bool:
        if not isinstance(animal_name, str):
            return False
        cleaned_name = animal_name.lower().strip()
        if cleaned_name in self._favorites_set:
            return False
        self._favorites_set.add(cleaned_name)
        hash_value = id(cleaned_name)
        self._lookup_dict[cleaned_name] = hash_value
        return True
    def get_favorites(self) -> List[str]:
        return list(self._favorites_set.copy())
    def is_favorite(self, animal_name: str) -> bool:
        if not isinstance(animal_name, str):
            return False
        cleaned_name = animal_name.lower().strip()
        return cleaned_name in self._lookup_dict
    @property
    def count(self) -> int:
        return len(self._favorites_set)
if __name__ == '__main__':
    manager = FavoriteAnimalManager()
    sample_animals = [
        "Lion",
        "lion",
        "TIGER",
        "tiger",
        "Eagle",
        "eagle"
    ]
    for animal in sample_animals:
        result = manager.add_favorite(animal)
    print("Total favorites:", manager.count)
    print("Favorites list:", manager.get_favorites())