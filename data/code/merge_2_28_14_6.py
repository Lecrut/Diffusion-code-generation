from typing import List
class AnimalTracker:
    def __init__(self) -> None:
        self.favorite_animals: set[str] = set()
    def add_favorite(self, animal_name: str | int | float) -> bool:
        try:
            if isinstance(animal_name, (int, float)):
                raise TypeError("Animal name must be a string.")
            normalized_name = animal_name.strip().lower()
            if not normalized_name or len(normalized_name) > 50:
                return False
            self.favorite_animals.add(normalized_name)
            return True
        except Exception as e:
            print(f"Error adding favorite animal: {e}")
            return False
    def get_favorites(self) -> List[str]:
        return sorted(list(self.favorite_animals))
if __name__ == '__main__':
    tracker = AnimalTracker()
    sample_data = [
        "Lion",
        123,
        "elephant",
        None,
        "",
        "Tiger",
        45.6,
        "Panda"
    ]
    for item in sample_data:
        tracker.add_favorite(item)
    print("Favorite Animals:", tracker.get_favorites())