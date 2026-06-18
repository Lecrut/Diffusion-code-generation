def count_animal_names(animal_list):
    counts = {}
    for animal in animal_list:
        if animal in counts:
            counts[animal] += 1
        else:
            counts[animal] = 1
    return counts
if __name__ == '__main__':
    sample_list = ["dog", "cat", "dog", "bird", "cat", "dog"]
    result = count_animal_names(sample_list)
    print(result)