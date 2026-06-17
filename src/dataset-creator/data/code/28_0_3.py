class AnimalManager:
    def __init__(self):
        self._favorites = []
    @staticmethod
    def validate_name(name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Animal name must be a non-empty string.")
        return name.capitalize()
    def add_favorite(self, animal_name):
        try:
            validated = self.validate_name(animal_name)
            if validated in self._favorites:
                print(f"{animal_name} is already in the list.")
            else:
                self._favorites.append(validated)
                return True
        except ValueError as e:
            print(str(e))
            return False
    def get_favorites(self):
        return sorted(self._favorites, key=str.lower)
if __name__ == '__main__':
    manager = AnimalManager()
    sample_data = [
        "lion",
        "Tiger",
        "elephant",
        "panda",
        "LION"
    ]
    for animal in sample_data:
        success = manager.add_favorite(animal)
    print("\nFinal List of Favorites:")
    if not manager.get_favorites():
        print("No favorites added.")
    else:
        for fav in manager.get_favorites():
            print(fav)