class AnimalGrouper:
    def __init__(self):
        self._grouped_animals = {}
    
    def add_animal(self, animal, legs):
        if legs not in self._grouped_animals:
            self._grouped_animals[legs] = []
        self._grouped_animals[legs].append(animal)
    
    def get_grouped_animals(self):
        return self._grouped_animals

if __name__ == '__main__':
    grouper = AnimalGrouper()
    sample_animals = {
        "dog": 4,
        "cat": 4,
        "spider": 8,
        "ant": 6,
        "bird": 2
    }
    for animal, legs in sample_animals.items():
        grouper.add_animal(animal, legs)
    
    print(grouper.get_grouped_animals())