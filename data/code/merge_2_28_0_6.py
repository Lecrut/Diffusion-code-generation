class AnimalManager:
    def __init__(self):
        self._favorites = []
    def add_animal(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Animal name must be a non-empty string.")
        normalized_name = name.capitalize()
        existing_names = [animal for animal in self._favorites]
        is_duplicate = any(animal.lower() == normalized_name.lower() for animal in existing_names)
        if not is_duplicate:
            self._favorites.append(normalized_name)
        else:
            raise ValueError(f"Animal '{name}' already exists.")
    def get_all_favorites(self):
        return list(self._favorites)
    def remove_animal(self, name):
        normalized_name = name.capitalize()
        try:
            index = self._favorites.index(normalized_name)
            del self._favorites[index]
            return True
        except ValueError:
            raise ValueError(f"Animal '{name}' not found.")
    def __len__(self):
        return len(self._favorites)
if __name__ == '__main__':
    manager = AnimalManager()
    sample_data = ["dog", "CAT", "elephant", "LION"]
    for animal in sample_data:
        try:
            manager.add_animal(animal)
        except ValueError as e:
            print(f"Error adding {animal}: {e}")
    print("Current favorites:", manager.get_all_favorites())