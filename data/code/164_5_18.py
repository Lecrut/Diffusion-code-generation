class AnimalDietClassifier:
    def __init__(self):
        self.diet_categories = {
            "herbivore": ["Cow", "Sheep", "Rabbit", "Panda"],
            "carnivore": ["Lion", "Tiger", "Bear", "Wolf"],
            "omnivore": ["Human", "Dog", "Cat", "Crow"]
        }

    def classify_animals(self, animals):
        classified_animals = {"herbivore": [], "carnivore": [], "omnivore": []}
        for animal in animals:
            if animal in self.diet_categories["herbivore"]:
                classified_animals["herbivore"].append(animal)
            elif animal in self.diet_categories["carnivore"]:
                classified_animals["carnivore"].append(animal)
            elif animal in self.diet_categories["omnivore"]:
                classified_animals["omnivore"].append(animal)
        return classified_animals

if __name__ == '__main__':
    classifier = AnimalDietClassifier()
    animals_to_classify = ["Cow", "Tiger", "Human", "Panda"]
    categorized_animals = classifier.classify_animals(animals_to_classify)
    print(categorized_animals)