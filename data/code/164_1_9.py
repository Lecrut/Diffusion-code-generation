class AnimalCategorizer:
    def __init__(self):
        self.animal_types = {
            "Mammal": ["Dog", "Cat"],
            "Bird": ["Eagle", "Crow"],
            "Fish": ["Salmon", "Tuna"]
        }

    def categorize_animals(self, raw_string):
        animal_dict = {}
        animals = raw_string.split(',')
        for animal in animals:
            animal_name = animal.strip()
            if animal_name:
                for animal_type, animal_list in self.animal_types.items():
                    if animal_name in animal_list:
                        if animal_type not in animal_dict:
                            animal_dict[animal_type] = []
                        animal_dict[animal_type].append(animal_name)
        return animal_dict

if __name__ == '__main__':
    categorizer = AnimalCategorizer()
    sample_input = "Dog,Cat,Eagle,Fish"
    result = categorizer.categorize_animals(sample_input)
    print(result)