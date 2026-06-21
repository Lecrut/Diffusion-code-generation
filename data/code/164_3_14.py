class AnimalClassifier:
    def __init__(self):
        self.domestic = {'dog': [], 'cat': [], 'bird': []}
        self.wild = {'lion': [], 'tiger': [], 'elephant': []}

    def classify(self, animals):
        for animal in animals:
            if animal in self.domestic:
                self.domestic[animal].append(animal)
            elif animal in self.wild:
                self.wild[animal].append(animal)

if __name__ == '__main__':
    classifier = AnimalClassifier()
    sample_animals = ['dog', 'lion', 'cat', 'tiger', 'bird']
    classifier.classify(sample_animals)
    print(classifier.domestic)
    print(classifier.wild)