class AnimalOrganizer:
    def __init__(self):
        self.animals = {}
    def add_animal(self, animal_type, animal_details):
        self.animals[animal_type] = animal_details
    def get_animal(self, animal_type):
        return self.animals.get(animal_type)
if __name__ == '__main__':
    organizer = AnimalOrganizer()
    organizer.add_animal("Dog", {"age": 5, "breed": "Labrador"})
    organizer.add_animal("Cat", {"age": 3, "breed": "Siamese"})
    organizer.add_animal("Bird", {"age": 2, "species": "Parrot"})
    print(organizer.get_animal("Dog"))
    print(organizer.get_animal("Cat"))
    print(organizer.get_animal("Fish"))