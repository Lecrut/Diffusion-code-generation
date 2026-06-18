def sort_unique_animals(animal_list):
    unique_set = set(animal_list)
    sorted_list = sorted(list(unique_set))
    return sorted_list
if __name__ == '__main__':
    sample_input = ["dog", "cat", "bird", "dog", "fish", "cat", "ant"]
    result = sort_unique_animals(sample_input)
    print(result)