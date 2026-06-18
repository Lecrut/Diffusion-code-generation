class AnimalManager:
    def __init__(self):
        self._favorites = []
    def add_favor(self, animal_name):
        if not isinstance(animal_name, str) or len(animal_name.strip()) == 0:
            raise ValueError("Invalid animal name")
        normalized = animal_name.capitalize()
        existing_names = [f.capitalize().strip() for f in self._favorites]
        if normalized.lower() in [name.lower() for name in existing_names]:
            return False
        self._favorites.append(normalized)
        return True
    def get_favorites(self):
        return list(self._favorites)
if __name__ == '__main__':
    manager = AnimalManager()
    sample_data = ["dog", "CAT", "elephant", "Lion"]
    for item in sample_data:
        result = manager.add_favor(item)
        print(f"Added {item}: {'Success' if result else 'Duplicate'}")
    final_list = manager.get_favorites()
    print("Final list:", final_list)