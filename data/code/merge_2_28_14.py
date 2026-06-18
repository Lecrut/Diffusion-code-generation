from typing import Any
class FavoriteAnimalTracker:
    def add_favorite(self, animal_name: str) -> None:
        if not isinstance(animal_name, str):
            raise TypeError(f"Invalid input type. Expected 'str', got {type(animal_name).__name__}")
        self._favorites[animal_name.lower()] = True
    def get_favorites(self) -> list[str]:
        return [key for key in self._favorites.keys() if isinstance(key, str)]
if __name__ == '__main__':
    tracker = FavoriteAnimalTracker()
    sample_data = ["lion", "elephant", 123, None, "tiger", "Lion"]
    try:
        for item in sample_data:
            if isinstance(item, (int, float)):
                print(f"Skipping invalid type {type(item).__name__} for animal name.")
                continue
            tracker.add_favorite(str(item))
        favorites = tracker.get_favorites()
        print("Favorite animals:", ", ".join(favorites))
    except Exception as e:
        print(f"An error occurred: {e}")