class AnimalCategorizer:
    ANIMAL_CATEGORIES = {
        "mammal": ["dog", "cat", "lion", "elephant"],
        "bird": ["bird"],
        "reptile": []
    }

    @staticmethod
    def categorize_animals(animal_list):
        animal_dict = {}
        for animal in animal_list:
            category = next((key for key, values in AnimalCategorizer.ANIMAL_CATEGORIES.items() if animal in values), "unknown")
            animal_dict[animal] = category
        return animal_dict

if __name__ == '__main__':
    animals = ["dog", "cat", "bird", "fish", "lion", "elephant"]
    categorized_animals = AnimalCategorizer.categorize_animals(animals)
    print(categorized_animals)