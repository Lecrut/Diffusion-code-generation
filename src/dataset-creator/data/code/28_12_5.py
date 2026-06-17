from typing import List
class FavoriteAnimalManager:
    def __init__(self) -> None:
        self._favorites: set[str] = set()
        self._history: list[str] = []
    def add_favorite(self, animal_name: str) -> bool:
        normalized_name = animal_name.lower().strip()
        if not normalized_name:
            return False
        if normalized_name in self._favorites:
            return False
        self._favorites.add(normalized_name)
        self._history.append(animal_name)
        return True
    def get_all_favorites(self) -> List[str]:
        return sorted(list(self._favorites))
    def remove_favorite(self, animal_name: str) -> bool:
        normalized_name = animal_name.lower().strip()
        if not self._favorites.discard(normalized_name):
            return False
        try:
            index = self._history.index(animal_name)
            del self._history[index]
        except ValueError:
            pass
        return True
    def get_count(self) -> int:
        return len(self._favorites)
if __name__ == '__main__':
    manager = FavoriteAnimalManager()
    sample_inputs = [
        "Lion",
        "lion",
        "TIGER",
        "  tiger ",
        "cat",
        "dog"
    ]
    for animal in sample_inputs:
        result = manager.add_favorite(animal)
        print(f"Added '{animal}': {result}")
    favorites = manager.get_all_favorites()
    print("\nCurrent Favorites:", favorites)
    remove_target = "CAT"
    removed = manager.remove_favorite(remove_target)
    print(f"\nRemoved '{remove_target}': {removed}")
    final_count = manager.get_count()
    print(f"\nTotal unique animals: {final_count}")