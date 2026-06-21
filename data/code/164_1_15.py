class AnimalCategorizer:
    def __init__(self):
        self.animal_dict = {}

    def add_animals(self, raw_string):
        animals = raw_string.split(',')
        for animal in animals:
            animal_name = animal.strip()
            if animal_name:
                if 'Mammal' not in self.animal_dict[animal_name]:
                    self.animal_dict.setdefault(animal_name, []).append('Mammal')
                if 'Vertebrate' not in self.animal_dict[animal_name]:
                    self.animal_dict[animal_name].append('Vertebrate')

    def get_animals_by_type(self):
        return self.animal_dict

if __name__ == '__main__':
    categorizer = AnimalCategorizer()
    sample_input = "Dog,Cat,Bird,Fish"
    categorizer.add_animals(sample_input)
    print(categorizer.get_animals_by_type())