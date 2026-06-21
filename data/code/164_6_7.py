class AnimalClassifier:
    def __init__(self):
        self.aquatic = []
        self.terrestrial = []
        self.aerial = []

    def classify(self, animal):
        if 'fish' in animal or 'sea' in animal:
            self.aquatic.append(animal)
        elif 'land' in animal or 'tree' in animal:
            self.terrestrial.append(animal)
        elif 'bird' in animal or 'fly' in animal:
            self.aerial.append(animal)

    def get_classification(self):
        return {'aquatic': self.aquatic, 'terrestrial': self.terrestrial, 'aerial': self.aerial}

if __name__ == '__main__':
    classifier = AnimalClassifier()
    animals = ['fish', 'lion', 'eagle', 'snake', 'dolphin', 'bear']
    for animal in animals:
        classifier.classify(animal)
    print(classifier.get_classification())