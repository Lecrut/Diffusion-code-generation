class AnimalCategory:
    SWIMMING = 'swimming'
    FLYING = 'flying'
    WALKING = 'walking'

    @staticmethod
    def categorize_animal(animal):
        if animal in ['Fish', 'Dolphin']:
            return AnimalCategory.SWIMMING
        elif animal in ['Bird', 'Eagle']:
            return AnimalCategory.FLYING
        elif animal in ['Dog', 'Cat']:
            return AnimalCategory.WALKING
        else:
            return None

if __name__ == '__main__':
    animals = ['Fish', 'Bird', 'Dog', 'Snake']
    categorized_animals = {animal: AnimalCategory.categorize_animal(animal) for animal in animals}
    print(categorized_animals)