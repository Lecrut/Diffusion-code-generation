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
            print(f"Animal: {name}, Type: {animal_type}")
        print("---------------------------")
    def display_by_type(self, animal_type):
        print(f"\n--- Animals of Type: {animal_type} ---")
        found = False
        for name, animal_type in self.animals.items():
            if animal_type == animal_type:
                print(f"{name}: {animal_type}")
                found = True
        if not found:
            print(f"No animals found of type {animal_type}.")
        print("------------------------------------")
def manage_and_display_animals():
    organizer = AnimalOrganizer()
    sample_data = [
        ("Leo", "Lion"),
        ("Molly", "Dog"),
        ("Bartholomew", "Cat"),
        ("Spot", "Dog"),
        ("Cleo", "Lion"),
        ("Rex", "Wolf")
    ]
    for name, animal_type in sample_data:
        organizer.add_animal(name, animal_type)
    organizer.display_all()
    print("\n--- Grouped by Type ---")
    unique_types = set(organizer.animals.values())
    for animal_type in sorted(list(unique_types)):
        organizer.display_by_type(animal_type)
if __name__ == '__main__':
    manage_and_display_animals()