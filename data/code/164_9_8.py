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
    def get_animal_type(self, name):
        return self.animals.get(name, "Animal not found")
if __name__ == '__main__':
    organizer = AnimalOrganizer()
    organizer.add_animal("Dog", "Canine")
    organizer.add_animal("Cat", "Feline")
    organizer.add_animal("Lion", "Feline")
    organizer.add_animal("Elephant", "Mammal")
    organizer.add_animal("Eagle", "Avian")
    organizer.display_all()
    print(f"\nType of Dog: {organizer.get_animal_type('Dog')}")
    print(f"Type of Snake: {organizer.get_animal_type('Snake')}")