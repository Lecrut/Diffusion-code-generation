def group_animals_by_legs(animals):
    grouped = {}
    for animal, legs in animals.items():
        if legs not in grouped:
            grouped[legs] = []
        grouped[legs].append(animal)
    return grouped

class AnimalGrouper:
    def __init__(self):
        self.grouped_animals = {}

    def add_animal(self, animal, legs):
        if legs not in self.grouped_animals:
            self.grouped_animals[legs] = []
        self.grouped_animals[legs].append(animal)

    def get_grouped_animals(self):
        return self.grouped_animals

if __name__ == '__main__':
    sample_animals = {
        "dog": 4,
        "cat": 4,
        "spider": 8,
        "ant": 6,
        "bird": 2
    }
    
    grouper = AnimalGrouper()
    for animal, legs in sample_animals.items():
        grouper.add_animal(animal, legs)
    
    grouped_animals = grouper.get_grouped_animals()
    print(grouped_animals)