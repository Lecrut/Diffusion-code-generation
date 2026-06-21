def filter_and_map(dictionary):
    filtered_dict = {}
    for key, value in dictionary.items():
        if isinstance(key, int) and isinstance(value, str):
            filtered_dict[key] = value
    return filtered_dict

if __name__ == '__main__':
    sample_dictionary = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five"
    }
    result = filter_and_map(sample_dictionary)
    print(result)