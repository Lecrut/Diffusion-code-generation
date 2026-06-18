def count_animal_names(animal_list):
    counts = {}
    for animal in animal_list:
        if animal in counts:
            counts[animal] += 1
        else:
            counts[animal] = 1
    return counts
if __name__ == '__main__':
    sample_list = ["cat", "dog", "cat", "bird", "dog", "cat"]
    result = count_animal_names(sample_list)
    print(result)