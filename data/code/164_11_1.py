class AnimalClassifier:
    def __init__(self):
        self.classification = {}
    def add_animal(self, order, animal_type):
        self.classification[order] = animal_type
    def get_animal_type(self, order):
        return self.classification.get(order)
if __name__ == '__main__':
    classifier = AnimalClassifier()
    classifier.add_animal("Mammalia", "Dog")
    classifier.add_animal("Aves", "Eagle")
    classifier.add_animal("Mammalia", "Cat")
    classifier.add_animal("Reptilia", "Snake")
    print(f"Type for Mammalia: {classifier.get_animal_type('Mammalia')}")
    print(f"Type for Aves: {classifier.get_animal_type('Aves')}")
    print(f"Type for Reptilia: {classifier.get_animal_type('Reptilia')}")
    print(f"Type for Pisces: {classifier.get_animal_type('Pisces')}")