class AnimalClassifier:
    def __init__(self):
        self.domestic_animals = {'Dog': [], 'Cat': []}
        self.wild_animals = {'Lion': [], 'Tiger': [], 'Elephant': []}

    def classify(self, animals):
        for animal in animals:
            if animal in self.domestic_animals:
                self.domestic_animals[animal].append(animal)
            elif animal in self.wild_animals:
                self.wild_animals[animal].append(animal)

if __name__ == '__main__':
    classifier = AnimalClassifier()
    sample_animals = ['Dog', 'Lion', 'Cat', 'Tiger', 'Bird']
    classifier.classify(sample_animals)
    print(classifier.domestic_animals)
    print(classifier.wild_animals)