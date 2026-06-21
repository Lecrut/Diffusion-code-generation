class AnimalClassifier:
    def __init__(self):
        self.domestic = {'Dog': [], 'Cat': [], 'Bird': [], 'Fish': []}
        self.wild = {'Lion': [], 'Tiger': [], 'Elephant': [], 'Giraffe': []}

    def classify(self, animals):
        for animal in animals:
            if animal in self.domestic:
                self.domestic[animal].append(animal)
            elif animal in self.wild:
                self.wild[animal].append(animal)

if __name__ == '__main__':
    classifier = AnimalClassifier()
    sample_animals = ['Dog', 'Lion', 'Cat', 'Tiger', 'Bird']
    classifier.classify(sample_animals)
    print(classifier.domestic)
    print(classifier.wild)