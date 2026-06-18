from typing import List
class FavoriteAnimalManager:
    def __init__(self) -> None:
        self._favorites: set[str] = set()
        self._history: list[str] = []
    def add_favorite(self, animal_name: str) -> bool:
        cleaned_name = animal_name.lower().strip()
        if not cleaned_name:
            return False
        is_duplicate = cleaned_name in self._favorites
        if not is_duplicate:
            self._favorites.add(cleaned_name)
            self._history.append(animal_name)
        return not is_duplicate
    def get_all_favorites(self) -> List[str]:
        return sorted(list(self._favorites))
    def remove_favorite(self, animal_name: str) -> bool:
        cleaned_name = animal_name.lower().strip()
        if cleaned_name in self._favorites:
            self._favorites.remove(cleaned_name)
            return True
        return False
if __name__ == '__main__':
    manager = FavoriteAnimalManager()
    sample_inputs = [
        "Lion",
        "lion",
        "Tiger",
        "  tiger ",
        "Bear"
    ]
    for animal in sample_inputs:
        result = manager.add_favorite(animal)
        print(f"Added '{animal}': {result}")
    all_favs = manager.get_all_favorites()
    print("All favorites:", all_favs)