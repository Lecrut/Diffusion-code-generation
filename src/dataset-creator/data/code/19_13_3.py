def sort_unique_animals(animal_list):
    unique_animals = set(animal_list)
    sorted_animals = sorted(list(unique_animals))
    return sorted_animals
if __name__ == '__main__':
    favorite_animals = ["dog", "cat", "bird", "dog", "fish", "cat", "bird"]
    result = sort_unique_animals(favorite_animals)
    print(result)