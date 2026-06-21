class AnimalClassifier:
    def __init__(self):
        self.aquatic = []
        self.terrestrial = []
        self.aerial = []

    def classify(self, animal):
        if 'fish' in animal or 'sea' in animal:
            return 'aquatic'
        elif 'land' in animal or 'tree' in animal:
            return 'terrestrial'
        elif 'bird' in animal or 'fly' in animal:
            return 'aerial'
        else:
            return None

    def classify_animals(self, animals):
        for animal in animals:
            classification = self.classify(animal)
            if classification == 'aquatic':
                self.aquatic.append(animal)
            elif classification == 'terrestrial':
                self.terrestrial.append(animal)
            elif classification == 'aerial':
                self.aerial.append(animal)

if __name__ == '__main__':
    classifier = AnimalClassifier()
    animals = ['fish', 'lion', 'eagle', 'snake', 'dolphin', 'bear']
    classifier.classify_animals(animals)
    print(classifier.get_classification())