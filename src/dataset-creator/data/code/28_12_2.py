from typing import List
class FavoriteAnimalManager:
    def __init__(self) -> None:
        self._favorites: set[str] = set()
        self._history: list[str] = []
    def add_favorites(self, animals: str | List[str]) -> int:
        cleaned_animals = [animal.lower().strip() for animal in (animals if isinstance(animals, list) else [animals])]
        added_count = 0
        for animal in cleaned_animals:
            if not self._favorites.discard(animal):
                self._history.append(animal)
                added_count += 1
        return added_count
    def get_all_favorites(self) -> List[str]:
        return list(self._favorites)
if __name__ == '__main__':
    manager = FavoriteAnimalManager()
    sample_input_1: str | List[str] = "Lion, Tiger"
    result_1 = manager.add_favorites(sample_input_1)
    sample_input_2: str | List[str] = ["lion", "tiger"]
    result_2 = manager.add_favorites(sample_input_2)
    print(f"Added from first input: {result_1}")
    print(f"Added from second input (duplicates handled): {result_2}")
    print("Current favorites:", manager.get_all_favorites())