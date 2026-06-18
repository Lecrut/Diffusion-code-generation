import re
def normalize_name(name):
    return name.strip().lower()
class AnimalTracker:
    def __init__(self):
        self.animals = set()
    def add_animal(self, animal_list):
        normalized_set = {normalize_name(animal) for animal in animal_list}
        self.animals.update(normalized_set)
    def get_unique_count(self):
        return len(list(set(str(x).lower().strip() if isinstance(x, str) else x)))
if __name__ == '__main__':
    tracker = AnimalTracker()
    sample_data_1 = ['Lion', 'Tiger', 'LEOPARD']
    sample_data_2 = {'panther', 'Panda'}
    tracker.add_animal(sample_data_1)
    tracker.add_animal(sample_data_2)
    unique_list = list(tracker.animals)
    print(f"Total Unique Animals: {len(unique_list)}")
    for animal in sorted(unique_list):
        print(animal.capitalize())