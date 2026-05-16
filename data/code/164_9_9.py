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
    organizer.add_animal("Leo", "Lion")
    organizer.add_animal("Molly", "Dog")
    organizer.add_animal("Toby", "Cat")
    organizer.add_animal("Simba", "Lion")
    organizer.add_animal("Bella", "Dog")
    organizer.add_animal("Whiskers", "Cat")
    organizer.display_all()
    organizer.display_by_type("Lion")
    organizer.display_by_type("Dog")
    organizer.display_by_type("Bird")
if __name__ == '__main__':
    manage_and_display_animals()