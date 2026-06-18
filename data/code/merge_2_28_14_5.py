class FavoriteAnimalTracker:
    def __init__(self):
        self._favorites = {}
    def add_favorite(self, animal_name) -> None:
        if not isinstance(animal_name, str):
            raise TypeError(f"Expected string type for animal name, got {type(animal_name).__name__}")
        normalized_name = animal_name.strip().lower()
        self._favorites[normalized_name] = True
    def get_favorites(self) -> set:
        return set(self._favorites.keys())
if __name__ == '__main__':
    tracker = FavoriteAnimalTracker()
    sample_data = [
        "Lion",
        123,
        "",
        None,
        "lion",
        "Tiger"
    ]
    for item in sample_data:
        try:
            tracker.add_favorite(item)
        except (TypeError, ValueError):
            continue
    print("Unique favorite animals:", tracker.get_favorites())