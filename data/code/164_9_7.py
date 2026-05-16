class AnimalOrganizer:
    def __init__(self):
        self.animals = {}
    def add_animal(self, animal_type, count):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
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
    organizer.add_animal("Dog", 5)
    organizer.add_animal("Cat", 8)
    organizer.add_animal("Bird", 12)
    organizer.add_animal("Fish", 3)
    organizer.add_animal("Dog", 2)
    organizer.display_organization()