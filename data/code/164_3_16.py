class AnimalClassifier:
    def __init__(self):
        self.domestic = {"Dog", "Cat", "Bird"}
        self.wild = {"Tiger", "Elephant", "Wolf"}

    def classify(self, animals):
        categorized_animals = {
            'domestic': [],
            'wild': []
        }
        for animal in animals:
            if animal in self.domestic:
                categorized_animals['domestic'].append(animal)
            elif animal in self.wild:
                categorized_animals['wild'].append(animal)
        return categorized_animals

if __name__ == '__main__':
    classifier = AnimalClassifier()
    sample_animals = ["Dog", "Cat", "Tiger", "Elephant"]
    result = classifier.classify(sample_animals)
    print(result)