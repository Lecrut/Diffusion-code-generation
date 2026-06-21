class AnimalCounter:
    def __init__(self):
        self.counts = {}

    @staticmethod
    def parse_animal_list(animals):
        return animals.split(',')

    @staticmethod
    def count_animals(animals):
        counter = AnimalCounter()
        for animal in animals:
            if animal not in counter.counts:
                counter.counts[animal] = 0
            counter.counts[animal] += 1
        return counter.counts

if __name__ == '__main__':
    sample_animals = "Dog, Cat, Dog, Bird, Fish, Bird"
    animals = AnimalCounter.parse_animal_list(sample_animals)
    result = AnimalCounter.count_animals(animals)
    print(result)