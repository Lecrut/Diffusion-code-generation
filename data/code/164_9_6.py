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
    organizer.add_animal("Lion", "Mammal")
    organizer.add_animal("Eagle", "Bird")
    organizer.add_animal("Whale", "Mammal")
    organizer.add_animal("Snake", "Reptile")
    organizer.add_animal("Parrot", "Bird")
    organizer.display_all()
    print("\n--- Specific Lookups ---")
    print(f"Lion's type: {organizer.get_animal_type('Lion')}")
    print(f"Elephant's type: {organizer.get_animal_type('Elephant')}")
    print(f"Fish's type: {organizer.get_animal_type('Fish')}")