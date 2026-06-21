def count_animals(animals):
    animal_count = {}
    for animal in animals:
        if animal in animal_count:
            animal_count[animal] += 1
        else:
            animal_count[animal] = 1
    return animal_count

if __name__ == '__main__':
    sample_data = ['dog', 'cat', 'bird', 'dog', 'fish', 'cat']
    print(count_animals(sample_data))