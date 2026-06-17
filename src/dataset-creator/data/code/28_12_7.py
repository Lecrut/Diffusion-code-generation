from typing import List
class FavoriteAnimalManager:
    def __init__(self) -> None:
        self._favorites: set[str] = set()
        self._history: list[str] = []
    def add_favorites(self, animals: str | List[str]) -> int:
        cleaned_animals: List[str] = [animal.lower().strip() for animal in (animals if isinstance(animals, list) else [animals])]
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
            raise TypeError("Animal must be a string")
        cleaned_animal = animal.lower().strip()
        if self._history and self._history[-1] == cleaned_animal:
            del self._history[-1]
        return cleaned_animal in self._favorites
    def get_count(self) -> int:
        return len(self._favorites)
if __name__ == '__main__':
    manager = FavoriteAnimalManager()
    sample_input_1 = "Lion, Tiger"
    count_1 = manager.add_favorites(sample_input_1)
    sample_input_2 = ["lion", "tiger", "elephant"]
    count_2 = manager.add_favorites(sample_input_2)
    favorites_list = manager.get_all_favorites()
    removed_status = False
    if len(favorites_list) > 0:
        animal_to_remove = sample_input_1.split(",")[0].lower().strip()
        for i in range(len(manager._history)):
            if manager._history[i] == animal_to_remove and not removed_status:
                manager.remove_favorite(animal_to_remove)
                removed_status = True
    print(f"Added {count_1} animals initially.")
    print(f"Total added including duplicates check: {count_2}")
    print(f"All favorites (sorted): {favorites_list}")
    if not removed_status and len(manager._history) > 0:
        animal_to_remove = manager._history[-1]
        for i in range(len(manager._history)):
            if manager._history[i] == animal_to_remove and not removed_status:
                manager.remove_favorite(animal_to_remove)
                removed_status = True
    print(f"Removed {animal_to_remove}: {removed_status}")