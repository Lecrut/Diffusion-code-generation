ANIMAL_TYPES = {
    "Mammalia": 1,
    "Aves": 2,
    "Reptilia": 3,
    "Amphibia": 4,
    "Pisces": 5,
}

def count_animal_types(animals):
    animal_count = {}
    for animal in animals:
        if animal in ANIMAL_TYPES:
            animal_type = ANIMAL_TYPES[animal]
            if animal_type not in animal_count:
                animal_count[animal_type] = 0
            animal_count[animal_type] += 1
    return animal_count

if __name__ == '__main__':
    animals = [
        "Mammalia", "Aves", "Mammalia", "Reptilia", "Amphibia",
        "Pisces", "Aves", "Mammalia", "Reptilia"
    ]
    result = count_animal_types(animals)
    print(result)