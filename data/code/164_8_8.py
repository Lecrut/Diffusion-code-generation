class AnimalClassifier:
    def __init__(self):
        self.endothermic = ['dog', 'cat', 'bird', 'lion', 'cow']
        self.ectothermic = ['fish', 'snake']

    def classify_animals(self, animals):
        result = {'endothermic': [], 'ectothermic': []}
        for animal in animals:
            if animal in self.endothermic:
                result['endothermic'].append(animal)
            elif animal in self.ectothermic:
                result['ectothermic'].append(animal)
        return result

if __name__ == '__main__':
    classifier = AnimalClassifier()
    sample_animals = ['dog', 'cat', 'bird', 'fish', 'lion', 'cow', 'snake']
    classified_animals = classifier.classify_animals(sample_animals)
    print("Endothermic:", classified_animals['endothermic'])
    print("Ectothermic:", classified_animals['ectothermic'])