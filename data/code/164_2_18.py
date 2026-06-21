class AnimalOrganizer:
    def __init__(self):
        self.animals = {}

    def add_animal(self, animal_type, habitat, details):
        if habitat not in self.animals:
            self.animals[habitat] = {}
        self.animals[habitat][animal_type] = details

    def get_animals_by_habitat(self, habitat):
        return self.animals.get(habitat, {})

if __name__ == '__main__':
    organizer = AnimalOrganizer()
    organizer.add_animal("Dog", "forest", {"age": 5, "breed": "Labrador"})
    organizer.add_animal("Cat", "desert", {"age": 3, "breed": "Siamese"})
    organizer.add_animal("Bird", "ocean", {"age": 7, "species": "Parrot"})
    print(organizer.get_animals_by_habitat("forest"))
    print(organizer.get_animals_by_habitat("desert"))
    print(organizer.get_animals_by_habitat("ocean"))