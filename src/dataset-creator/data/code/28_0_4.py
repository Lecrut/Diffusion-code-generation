class AnimalManager:
    def __init__(self):
        self._favorites = []
    def add_animal(self, animal_name):
        if not isinstance(animal_name, str) or len(animal_name.strip()) == 0:
            raise ValueError("Animal name must be a non-empty string.")
        normalized_name = animal_name.strip().capitalize()
        existing_names = [name.capitalize() for name in self._favorites]
        if normalized_name not in existing_names and normalized_name.lower() not in [n.lower() for n in self._favorites]:
            self._favorites.append(normalized_name)
        else:
            raise ValueError(f"Animal '{animal_name}' already exists or is invalid.")
    def get_favorites(self):
        return list(self._favorites)
    def remove_animal(self, animal_name):
        if not isinstance(animal_name, str):
            raise ValueError("Invalid input type for removal.")
        target = animal_name.strip().capitalize()
        try:
            self._favorites.remove(target)
        except ValueError:
            raise ValueError(f"Animal '{animal_name}' not found in favorites list.")
    def count_favorites(self):
        return len(self._favorites)
if __name__ == '__main__':
    manager = AnimalManager()
    sample_data = [
        "dog",
        "cat",
        "lion",
        "tiger",
        "panda"
    ]
    for animal in sample_data:
        try:
            manager.add_animal(animal)
        except ValueError as e:
            print(f"Error adding '{animal}': {e}")
    print("Current favorites:")
    for name in manager.get_favorites():
        print(name)
    print("\nTotal count:", manager.count_favorites())