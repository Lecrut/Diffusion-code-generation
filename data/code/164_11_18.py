def count_animal_types(animal_list):
    animal_count = {}
    for animal in animal_list:
        if animal in animal_count:
            animal_count[animal] += 1
        else:
            animal_count[animal] = 1
    return animal_count

if __name__ == '__main__':
    animals = ["Dog", "Eagle", "Whale", "Snake", "Cat"]
    result = count_animal_types(animals)
    print(result)