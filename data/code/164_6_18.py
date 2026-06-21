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
        classification = {'aquatic': [], 'terrestrial': [], 'aerial': []}
        for animal in animals:
            result = self.classify(animal)
            if result:
                classification[result].append(animal)
        return classification

if __name__ == '__main__':
    classifier = AnimalClassifier()
    animals = ['fish', 'dog', 'bird', 'frog', 'eagle']
    print(classifier.classify_animals(animals))