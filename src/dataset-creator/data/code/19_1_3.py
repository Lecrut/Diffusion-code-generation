class AnimalTracker:
    def __init__(self):
        self.favorites = []
    def add_animal(self, animal_name):
        if animal_name not in self.favorites:
            self.favorites.append(animal_name)
    def get_animals(self):
        return self.favorites
    def display_animals(self):
        print("Favorite Animals:")
        for animal in self.favorites:
            print(animal)
if __name__ == '__main__':
    tracker = AnimalTracker()
    tracker.add_animal("Dog")
    tracker.add_animal("Cat")
    tracker.add_animal("Bird")
    tracker.add_animal("Dog")
    tracker.add_animal("Fish")
    tracker.display_animals()