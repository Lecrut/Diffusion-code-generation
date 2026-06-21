class AnimalClassifier:
    def classify(self, animal):
        if 'fish' in animal.lower() or 'sea' in animal.lower():
            return 'aquatic'
        elif 'bird' in animal.lower() or 'winged' in animal.lower():
            return 'aerial'
        else:
            return 'terrestrial'

    def classify_animals(self, animals):
        aquatic = []
        terrestrial = []
        aerial = []
        for animal in animals:
            classification = self.classify(animal)
            if classification == 'aquatic':
                aquatic.append(animal)
            elif classification == 'terrestrial':
                terrestrial.append(animal)
            elif classification == 'aerial':
                aerial.append(animal)
        return {'aquatic': aquatic, 'terrestrial': terrestrial, 'aerial': aerial}

if __name__ == '__main__':
    classifier = AnimalClassifier()
    animals = ['fish', 'tiger', 'bird', 'snake', 'eagle', 'frog']
    print(classifier.classify_animals(animals))