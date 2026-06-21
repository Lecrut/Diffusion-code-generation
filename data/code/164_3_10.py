class AnimalClassifier:
    def __init__(self):
        self.domestic_animals = {'dog', 'cat', 'bird'}
        self.wild_animals = {'lion', 'tiger', 'elephant'}

    def classify(self, animals):
        classification = {'domestic': [], 'wild': []}
        for animal in animals:
            if animal.lower() in self.domestic_animals:
                classification['domestic'].append(animal)
            elif animal.lower() in self.wild_animals:
                classification['wild'].append(animal)
        return classification

if __name__ == '__main__':
    classifier = AnimalClassifier()
    sample_animals = ['dog', 'lion', 'cat', 'tiger', 'bird']
    print(classifier.classify(sample_animals))