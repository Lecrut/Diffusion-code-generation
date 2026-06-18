def sort_unique_animals(animal_list):
    unique_set = set(animal_list)
    sorted_list = sorted(list(unique_set))
    return sorted_list
if __name__ == '__main__':
    sample_animals = ["dog", "cat", "bird", "dog", "fish", "cat", "bird"]
    result = sort_unique_animals(sample_animals)
    print(result)