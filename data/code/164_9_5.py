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
            print(f"Name: {name}, Type: {animal_type}")
        print("---------------------------")
    def get_animal_type(self, name):
        return self.animals.get(name, "Animal not found")
if __name__ == '__main__':
    organizer = AnimalOrganizer()
    organizer.add_animal("Leo", "Lion")
    organizer.add_animal("Molly", "Dog")
    organizer.add_animal("Toby", "Rabbit")
    organizer.add_animal("Bartholomew", "Bear")
    organizer.display_all()
    print("\n--- Specific Queries ---")
    print(f"Type of Leo: {organizer.get_animal_type('Leo')}")
    print(f"Type of Fido: {organizer.get_animal_type('Fido')}")
    print(f"Type of Unknown: {organizer.get_animal_type('Fido')}")