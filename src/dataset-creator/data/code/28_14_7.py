from typing import List
class AnimalTracker:
    def __init__(self) -> None:
        self.favorites: dict[str, int] = {}
    def add_favorite(self, animal_name: str | object) -> bool:
        if not isinstance(animal_name, str):
            raise TypeError(f"Expected string input for animal name, got {type(animal_name).__name__}")
        lowercased_name = animal_name.lower().strip()
        if lowercased_name in self.favorites:
            return False
        self.favorites[lowercased_name] = 1
        return True
def get_favorite_count(tracker: AnimalTracker) -> int:
    return len(tracker.favorites)
if __name__ == '__main__':
    tracker = AnimalTracker()
    sample_inputs = [
        "Lion",
        "Tiger",
        123,
        "lion",
        None,
        "Bear"
    ]
    for item in sample_inputs:
        try:
            result = tracker.add_favorite(item)
            print(f"{item!r} -> Added: {result}")
        except TypeError as e:
            print(f"Error with {item!r}: {e}")
    print(f"\nTotal unique favorites tracked: {get_favorite_count(tracker)}")