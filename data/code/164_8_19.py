class AnimalClassifier:
    ENDOTHERMIC_ANIMALS = {'dog', 'cat', 'bird', 'cow'}
    ECTOTHERMIC_ANIMALS = {'fish', 'snake'}

    @staticmethod
    def classify_animals(animals):
        result = {
            'endothermic': [],
            'ectothermic': []
        }
        for animal in animals:
            if animal in AnimalClassifier.ENDOTHERMIC_ANIMALS:
                result['endothermic'].append(animal)
            elif animal in AnimalClassifier.ECTOTHERMIC_ANIMALS:
                result['ectothermic'].append(animal)
        return result

if __name__ == '__main__':
    sample_animals = ['dog', 'cat', 'bird', 'fish', 'lion', 'cow', 'snake']
    classified_animals = AnimalClassifier.classify_animals(sample_animals)
    print(classified_animals)