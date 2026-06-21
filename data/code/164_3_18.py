class AnimalClassifier:
    def __init__(self):
        self.domestic = {'dog', 'cat', 'bird'}
        self.wild = {'lion', 'tiger', 'elephant'}

    def classify_animals(self, animals):
        classification = {'domestic': [], 'wild': []}
        for animal in animals:
            if animal in self.domestic:
                classification['domestic'].append(animal)
            elif animal in self.wild:
                classification['wild'].append(animal)
        return classification

if __name__ == '__main__':
    classifier = AnimalClassifier()
    sample_animals = ['dog', 'lion', 'cat', 'tiger', 'bird']
    print(classifier.classify_animals(sample_animals))