class AnimalClassifier:
    def __init__(self):
        self.classification = {}
    def add_animal(self, biological_order, animal_type):
        self.classification[biological_order] = animal_type
    def get_animal_type(self, biological_order):
        return self.classification.get(biological_order, "Not Found")
if __name__ == '__main__':
    classifier = AnimalClassifier()
    classifier.add_animal("Mammalia", "Dog")
    classifier.add_animal("Aves", "Eagle")
    classifier.add_animal("Chordata", "Whale")
    classifier.add_animal("Mammalia", "Cat")
    print(f"Type for Mammalia: {classifier.get_animal_type('Mammalia')}")
    print(f"Type for Aves: {classifier.get_animal_type('Aves')}")
    print(f"Type for Reptilia: {classifier.get_animal_type('Reptilia')}")