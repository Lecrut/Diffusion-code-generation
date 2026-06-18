class AnimalTracker:
    def __init__(self):
        self.favorites = set()
    def add_favorite(self, animal_name):
        self.favorites.add(animal_name)
if __name__ == '__main__':
    tracker = AnimalTracker()
    print("Initial favorites:", tracker.favorites)
    tracker.add_favorite("Dog")
    print("After adding Dog:", tracker.favorites)
    tracker.add_favorite("Cat")
    print("After adding Cat:", tracker.favorites)
    tracker.add_favorite("Dog")
    print("After adding duplicate Dog:", tracker.favorites)