class AnimalOrganizer:
    def __init__(self):
        self.habitats = {}

    def add_animal(self, animal_type, habitat):
        if habitat not in self.habitats:
            self.habitats[habitat] = []
        self.habitats[habitat].append(animal_type)

    def get_habitat(self, habitat):
        return self.habitats.get(habitat, [])

if __name__ == '__main__':
    organizer = AnimalOrganizer()
    organizer.add_animal("Dog", "forest")
    organizer.add_animal("Cat", "desert")
    organizer.add_animal("Fish", "ocean")
    organizer.add_animal("Bird", "forest")
    print(organizer.get_habitat("forest"))
    print(organizer.get_habitat("ocean"))
    print(organizer.get_habitat("desert"))