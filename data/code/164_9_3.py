class AnimalOrganizer:
    def __init__(self):
        self.animals = {}
    def add_animal(self, name, type):
        self.animals[name] = type
    def display_all(self):
        print("--- Animal Organization ---")
        if not self.animals:
            print("No animals currently organized.")
            return
        for name, animal_type in self.animals.items():
            print(f"{name}: {animal_type}")
        print("---------------------------")
    def display_by_type(self, animal_type):
        print(f"\n--- Animals of type {animal_type} ---")
        found = False
        for name, animal_type in self.animals.items():
            if animal_type == animal_type:
                print(f"{name}: {animal_type}")
                found = True
        if not found:
            print(f"No animals found of type {animal_type}.")
        print("----------------------------------")
if __name__ == '__main__':
    organizer = AnimalOrganizer()
    organizer.add_animal("Leo", "Mammal")
    organizer.add_animal("Whale", "Mammal")
    organizer.add_animal("Eagle", "Bird")
    organizer.add_animal("Shark", "Fish")
    organizer.add_animal("Parrot", "Bird")
    organizer.add_animal("Dolphin", "Mammal")
    organizer.display_all()
    organizer.display_by_type("Mammal")
    organizer.display_by_type("Bird")
    organizer.display_by_type("Reptile")