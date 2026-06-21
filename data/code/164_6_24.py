class AnimalClassifier:
    def classify(self, animal):
        if 'fish' in animal or 'sea' in animal:
            return 'aquatic'
        elif 'land' in animal or 'forest' in animal:
            return 'terrestrial'
        elif 'bird' in animal or 'fly' in animal:
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
    result = classifier.classify_animals(animals)
    print(result)