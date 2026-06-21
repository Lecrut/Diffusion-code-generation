def count_animals(animal_list):
    animal_count = {}
    for animal in animal_list:
        if animal in animal_count:
            animal_count[animal] += 1
        else:
            animal_count[animal] = 1
    return animal_count

if __name__ == '__main__':
    animals = ["Cat", "Dog", "Bird", "Fish", "Dog", "Cat"]
    result = count_animals(animals)
    print(f"Animal counts: {result}")