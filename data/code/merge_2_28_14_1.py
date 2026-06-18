from typing import Dict, List
class AnimalTracker:
    def __init__(self) -> None:
        self._favorites: set[str] = set()
    def add_favorite(self, animal_name: str | int | float) -> bool:
        try:
            if not isinstance(animal_name, (str,)):
                raise TypeError("Animal name must be a string.")
            normalized_name = animal_name.strip().lower()
            if not normalized_name or len(normalized_name) > 50:
                return False
            self._favorites.add(normalized_name)
            return True
        except Exception as e:
            print(f"Error adding favorite: {e}")
            return False
    def get_favorites(self) -> List[str]:
        return sorted(list(self._favorites))
if __name__ == '__main__':
    tracker = AnimalTracker()
    sample_data = [
        "Lion",
        123,
        -45.67,
        "",
        None,
        "Tiger",
        "tiger",
        "Elephant"
    ]
    for item in sample_data:
        tracker.add_favorite(item)
    print("Favorite Animals:", tracker.get_favorites())