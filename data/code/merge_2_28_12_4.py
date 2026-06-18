from typing import List
class FavoriteAnimalManager:
    def __init__(self) -> None:
        self._favorites: set[str] = set()
        self._history: list[str] = []
    def add_favorites(self, animals: str | List[str]) -> int:
        cleaned_animals = [animal.lower().strip() for animal in (animals if isinstance(animals, list) else [animals])]
        count_added = 0
        for animal in cleaned_animals:
            if not self._favorites.add(animal):
                continue
            self._history.append(animal)
            count_added += 1
        return count_added
    def get_all_favorites(self) -> List[str]:
        return list(self._favorites.copy())
if __name__ == '__main__':
    manager = FavoriteAnimalManager()
    sample_input_1: str | List[str] = "Lion, Tiger"
    result_count_1 = manager.add_favorites(sample_input_1)
    sample_input_2: str | List[str] = ["lion", "tiger"]
    result_count_2 = manager.add_favorites(sample_input_2)
    print(f"Added from first input: {result_count_1}")
    print(f"Added from second input (duplicates handled): {result_count_2}")
    all_animals = manager.get_all_favorites()
    print(f"All favorites: {all_animals}")