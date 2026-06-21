class AnimalClassifier:
    def __init__(self):
        self.domestic = {'Dog': None, 'Cat': None, 'Bird': None}
        self.wild = {'Lion': None, 'Tiger': None, 'Elephant': None}

    def classify(self, animals):
        result = {'domestic': [], 'wild': []}
        for animal in animals:
            if animal in self.domestic:
                result['domestic'].append(animal)
            elif animal in self.wild:
                result['wild'].append(animal)
        return result

if __name__ == '__main__':
    classifier = AnimalClassifier()
    sample_animals = ['Dog', 'Lion', 'Cat', 'Tiger', 'Bird']
    print(classifier.classify(sample_animals))