class AnimalClassifier:
    def __init__(self):
        self.classification = {}
    def add_animal(self, biological_order, animal_type):
        if biological_order not in self.classification:
            self.classification[biological_order] = []
        self.classification[biological_order].append(animal_type)
    def get_animals_by_order(self, biological_order):
        return self.classification.get(biological_order, [])
if __name__ == '__main__':
    classifier = AnimalClassifier()
    classifier.add_animal("Mammalia", "Dog")
    classifier.add_animal("Mammalia", "Cat")
    classifier.add_animal("Aves", "Eagle")
    classifier.add_animal("Mammalia", "Whale")
    classifier.add_animal("Reptilia", "Snake")
    print(classifier.get_animals_by_order("Mammalia"))
    print(classifier.get_animals_by_order("Aves"))
    print(classifier.get_animals_by_order("Amphibia"))