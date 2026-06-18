import re
def normalize_name(name):
    return name.lower().strip()
class AnimalTracker:
    def __init__(self):
        self.animals = set()
    def add_animal(self, animal_list):
        normalized_names = [normalize_name(animal) for animal in animal_list]
        self.animals.update(normalized_names)
    def get_unique_animals(self):
        return list(self.animals)
if __name__ == '__main__':
    tracker = AnimalTracker()
    sample_lists = ['Lion', 'Tiger', 'LEOPARD']
    sample_sets = {'bear', 'Wolf'}
    mixed_input = [  'Giraffe\n', 'Panda' ]
    tracker.add_animal(sample_lists)
    tracker.add_animal(sample_sets)
    tracker.add_animal(mixed_input)
    unique_results = tracker.get_unique_animals()
    for animal in sorted(unique_results):
        print(animal)