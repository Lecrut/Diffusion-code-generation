class AnimalManager:
    def __init__(self):
        self._favorites = []
    def add_animal(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Animal name must be a non-empty string.")
        clean_name = name.strip().capitalize()
        existing_names = [a.capitalize() for a in self._favorites]
        if clean_name.lower() in [x.lower() for x in existing_names]:
            return False
        self._favorites.append(clean_name)
        return True
    def get_favorites(self):
        return list(self._favorites)
    def remove_animal(self, name):
        target = name.strip().capitalize() if isinstance(name, str) else None
        for i, animal in enumerate(self._favorites):
            if animal.lower() == target.lower():
                self._favorites.pop(i)
                return True
        return False
    def __len__(self):
        return len(self._favorites)
if __name__ == '__main__':
    manager = AnimalManager()
    sample_data = [
        "python",
        "Lion",
        "elephant",
        "tiger",
        "dog"
    ]
    for item in sample_data:
        result = manager.add_animal(item)
        print(f"Added '{item}': {result}")
    current_list = manager.get_favorites()
    print("\nCurrent favorites:")
    for animal in current_list:
        print(animal)