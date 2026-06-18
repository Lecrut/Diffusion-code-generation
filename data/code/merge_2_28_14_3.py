from typing import List
class AnimalTracker:
    def __init__(self) -> None:
        self._favorites: dict[str, int] = {}
    def add_favorite(self, animal_name: str | object) -> bool:
        if not isinstance(animal_name, str):
            raise TypeError(f"Expected string input for animal name, got {type(animal_name).__name__}")
        current_count = self._favorites.get(animal_name, 0) + 1
        self._favorites[animal_name] = current_count
        return True
    def get_favorite_names(self) -> List[str]:
        return list(self._favorites.keys())
if __name__ == '__main__':
    tracker = AnimalTracker()
    sample_data: List[tuple[str, object]] = [
        ("Lion", "string"),
        (123, int),                      
        ("Tiger", "string"),
        ("Elephant", None),                             
        ("Panda", "string")
    ]
    for name, value in sample_data:
        try:
            tracker.add_favorite(name)
        except TypeError as e:
            print(f"Error adding {name}: {e}")
    print("Favorite animals:", tracker.get_favorite_names())