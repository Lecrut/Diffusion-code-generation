class AnimalTracker:
    def __init__(self):
        self.favorites = set()
    def add_favorite(self, animal_name):
        self.favorites.add(animal_name)
if __name__ == '__main__':
    tracker = AnimalTracker()
    print(f"Initial favorites: {tracker.favorites}")
    tracker.add_favorite("Dog")
    print(f"After adding Dog: {tracker.favorites}")
    tracker.add_favorite("Cat")
    print(f"After adding Cat: {tracker.favorites}")
    tracker.add_favorite("Dog")
    print(f"After adding Dog again (no change): {tracker.favorites}")
    tracker.add_favorite("Bird")
    print(f"After adding Bird: {tracker.favorites}")