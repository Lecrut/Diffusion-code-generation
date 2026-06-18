from typing import List
class FavoriteAnimalManager:
    def __init__(self) -> None:
        self._favorites: set[str] = set()
        self._history: list[str] = []
    def add_favorites(self, animals: str | List[str]) -> int:
        cleaned_animals = [a.lower().strip() for a in (animals if isinstance(animals, list) else [animals])]
        added_count = 0
        for animal in cleaned_animals:
            if animal not in self._favorites and animal != "":
                self._favorites.add(animal)
                self._history.append(animal)
                added_count += 1
        return added_count
    def get_all_favorites(self) -> List[str]:
        return sorted(list(self._favorites))
    def remove_favorite(self, animal: str | None = None) -> bool:
        if not isinstance(animal, str):
            return False
        cleaned_animal = animal.lower().strip()
        if cleaned_animal in self._favorites:
            self._favorites.remove(cleaned_animal)
            try:
                index = self._history.index(cleaned_animal)
                del self._history[index]
            except ValueError:
                pass
            return True
        return False
    def get_count(self) -> int:
        return len(self._favorites)
if __name__ == '__main__':
    manager = FavoriteAnimalManager()
    result1 = manager.add_favorites("Lion, Tiger")
    print(f"Added {result1} new favorites.")
    all_animals = manager.get_all_favorites()
    print(all_animals)
    count = manager.remove_favorite("lion")
    print(f"Removed lion: {count}")
    final_count = manager.get_count()
    print(final_count)