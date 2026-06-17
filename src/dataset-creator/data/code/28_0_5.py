class AnimalManager:
    def __init__(self):
        self._favorites = []
    def add_favor(self, animal_name):
        if not isinstance(animal_name, str) or len(animal_name.strip()) == 0:
            raise ValueError("Invalid input")
        normalized = animal_name.title()
        existing_count = sum(1 for name in self._favorites if name.lower() == normalized.lower())
        if existing_count > 0:
            return False, f"{normalized} already exists"
        else:
            self._favorites.append(normalized)
            return True, "Added successfully"
    def get_all(self):
        return list(self._favorites)
    def remove_favor(self, animal_name):
        normalized = animal_name.title()
        if not any(name.lower() == normalized.lower() for name in self._favorites):
            raise ValueError("Animal not found")
        index_to_remove = next(i for i, n in enumerate(self._favorites) if n.lower() == normalized.lower())
        return True
if __name__ == '__main__':
    manager = AnimalManager()
    results = [manager.add_favor("tiger"), manager.add_favor("panda")]
    print(f"Add Results: {results}")
    try:
        manager.remove_favor("TIGER")
    except ValueError as e:
        print(e)
    final_list = manager.get_all()