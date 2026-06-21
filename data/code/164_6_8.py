class AnimalClassifier:
    def classify(self, animal):
        if 'fin' in animal or 'swim' in animal:
            return 'aquatic'
        elif 'leg' in animal or 'walk' in animal:
            return 'terrestrial'
        elif 'wing' in animal or 'fly' in animal:
            return 'aerial'
        else:
            return None

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
    animals = ['shark', 'lion', 'eagle']
    print(classifier.classify_animals(animals))