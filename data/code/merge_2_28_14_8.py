class AnimalTracker:
    def __init__(self):
        self.favorites = {}
    def add_favorite(self, animal_name):
        if not isinstance(animal_name, str) or len(animal_name.strip()) == 0:
            raise ValueError("Invalid input: Must be a non-empty string.")
        name_stripped = animal_name.strip()
        self.favorites[name_stripped] = True
    def get_count(self):
        return len(self.favorites)
if __name__ == '__main__':
    tracker = AnimalTracker()
    sample_inputs = [
        "Lion",
        123,
        "",
        None,
        "Tiger",
        "   Elephant   ",
        True,
        "Panda"
    ]
    for item in sample_inputs:
        try:
            tracker.add_favorite(item)
            print(f"Added successfully.")
        except ValueError as e:
            print(f"Error adding {item}: {e}")
print("\nTotal unique favorites:", tracker.get_count())