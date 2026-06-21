class AnimalClassifier:
    def __init__(self):
        self.domestic = {'Dog': True, 'Cat': True, 'Bird': True, 'Fish': True}
        self.wild = {'Lion': True, 'Tiger': True, 'Elephant': True, 'Rhino': True}

    def classify(self, animals):
        classification = {'domestic': [], 'wild': []}
        for animal in animals:
            if animal in self.domestic:
                classification['domestic'].append(animal)
            elif animal in self.wild:
                classification['wild'].append(animal)
        return classification

if __name__ == '__main__':
    classifier = AnimalClassifier()
    sample_animals = ['Dog', 'Lion', 'Cat', 'Tiger', 'Bird']
    print(classifier.classify(sample_animals))