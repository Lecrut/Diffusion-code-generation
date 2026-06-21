class AnimalClassifier:
    def __init__(self):
        self.aquatic = []
        self.terrestrial = []
        self.aerial = []

    def classify(self, animal):
        if 'fish' in animal or 'sea' in animal:
            return 'aquatic'
        elif 'land' in animal or 'forest' in animal:
            return 'terrestrial'
        elif 'bird' in animal or 'wing' in animal:
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
    animals = ['fish', 'lion', 'bird', 'snake', 'dolphin', 'bear', 'eagle']
    classifier.classify_animals(animals)
    print({'aquatic': classifier.aquatic, 'terrestrial': classifier.terrestrial, 'aerial': classifier.aerial})