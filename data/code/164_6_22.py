class AnimalClassifier:
    def classify(self, animal):
        if any(keyword in animal for keyword in ('fish', 'sea', 'ocean')):
            return 'aquatic'
        elif any(keyword in animal for keyword in ('land', 'forest', 'grassland')):
            return 'terrestrial'
        elif any(keyword in animal for keyword in ('bird', 'wing', 'fly')):
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
    animals = ['fish', 'tiger', 'eagle', 'snake', 'dolphin', 'bear']
    print(classifier.classify_animals(animals))