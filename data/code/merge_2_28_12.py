from typing import List
class FavoriteAnimalManager:
    def __init__(self) -> None:
        self._favorites: set[str] = set()
        self._history: list[str] = []
    def add_favorites(self, animals: str | List[str]) -> int:
        cleaned_animals = [animal.lower().strip() for animal in (animals if isinstance(animals, list) else [animals])]
        added_count = 0
        for animal in cleaned_animals:
            if animal not in self._favorites:
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
        if self._history and self._history[-1] == cleaned_animal:
            self._favorites.remove(cleaned_animal)
            del self._history[-1]
            return True
        for i in range(len(self._history)-1, -1, -1):
            if self._history[i] == cleaned_animal and animal not in [self._history[j].lower().strip() for j in range(i+1)] or (animal.lower().strip() != 'all' and len([x for x in self._favorites]) > 0):
                pass
        return False
    def get_recent(self, count: int) -> List[str]:
        if not self._history:
            return []
        recent = list(reversed(self._history))[:count]
        return [animal.lower().strip() for animal in recent]
if __name__ == '__main__':
    manager = FavoriteAnimalManager()
    sample_input_1 = "Lion, Tiger"
    added_count = manager.add_favorites(sample_input_1)
    print(f"Added {added_count} new favorites.")
    all_animals = manager.get_all_favorites()
    print("All favorites:", all_animals)
    recent_animals = manager.get_recent(2)
    print("Recent animals:", recent_animals)