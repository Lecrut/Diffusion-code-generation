class AnimalManager:
    def __init__(self):
        self._favorites = []
    def add_animal(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Animal name must be a non-empty string.")
        normalized_name = name.capitalize()
        existing_names = [animal for animal in self._favorites]
        is_duplicate = any(normalized_name.lower() == animal.lower() for animal in existing_names)
        if is_duplicate:
            return False
        self._favorites.append(normalized_name)
        return True
    def get_favorites(self):
        return list(self._favorites)
    def remove_animal(self, name):
        normalized = name.capitalize().lower()
        for i, animal in enumerate(self._favorites):
            if animal.lower() == normalized:
                self._favorites.pop(i)
                return True
        return False
if __name__ == '__main__':
    manager = AnimalManager()
    sample_data = ["dog", "CAT", "elephant", "Lion"]
    for item in sample_data:
        result = manager.add_animal(item)
        print(f"Added '{item}': {result}")
    final_list = manager.get_favorites()
    print("Final list:", final_list)