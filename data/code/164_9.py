class AnimalOrganizer:
    def __init__(self):
        self.animals = {}
    def add_animal(self, animal_type, count):
        if animal_type not in self.animals:
            self.animals[animal_type] = 0
        self.animals[animal_type] += count
    def display_organization(self):
        if not self.animals:
            print("No animal data to display.")
            return
        print("--- Animal Organization ---")
        sorted_animals = sorted(self.animals.items())
        for animal, count in sorted_animals:
            print(f"{animal}: {count}")
        print("---------------------------")
if __name__ == '__main__':
    organizer = AnimalOrganizer()
    organizer.add_animal("Dog", 15)
    organizer.add_animal("Cat", 22)
    organizer.add_animal("Bird", 8)
    organizer.add_animal("Fish", 30)
    organizer.add_animal("Rabbit", 12)
    organizer.display_organization()