from collections import defaultdict

ANIMAL_COUNTS = {}

def count_animals(animals):
    global ANIMAL_COUNTS
    for animal in animals:
        if animal in ANIMAL_COUNTS:
            ANIMAL_COUNTS[animal] += 1
        else:
            ANIMAL_COUNTS[animal] = 1
    return ANIMAL_COUNTS

if __name__ == '__main__':
    sample_animals = ["Dog", "Eagle", "Whale", "Snake", "Cat", "Dog"]
    result = count_animals(sample_animals)
    print(result)