def concatenate_strings(string_list, delimiter):
    return ''.join([f"{s}{delimiter}" for s in string_list])[:-len(delimiter)]

if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry"]
    separator = ", "
    combined_fruits = concatenate_strings(fruits, separator)
    print(combined_fruits)

    animals = ["dog", "cat", "bird"]
    animal_separator = "; "
    combined_animals = concatenate_strings(animals, animal_separator)
    print(combined_animals)