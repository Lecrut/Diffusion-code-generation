class Animal:
    def __init__(self, name, locomotion):
        self.name = name
        self.locomotion = locomotion

    def get_locomotion(self):
        return self.locomotion

class AnimalCategorizer:
    def __init__(self):
        self.categories = {'swimming': [], 'flying': [], 'walking': []}

    def add_animal(self, animal):
        category = animal.get_locomotion()
        if category in self.categories:
            self.categories[category].append(animal.name)

    def get_categories(self):
        return self.categories

if __name__ == '__main__':
    categorizer = AnimalCategorizer()
    animals = [
        Animal("Fish", "swimming"),
        Animal("Eagle", "flying"),
        Animal("Dog", "walking"),
        Animal("Penguin", "swimming"),
        Animal("Bat", "flying")
    ]
    
    for animal in animals:
        categorizer.add_animal(animal)
    
    categories = categorizer.get_categories()
    print(f"Swimming: {categories['swimming']}")
    print(f"Flying: {categories['flying']}")
    print(f"Walking: {categories['walking']}")