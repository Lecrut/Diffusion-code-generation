def map_dict_to_strings(input_dict):
    return {key: value for key, value in input_dict.items() if isinstance(value, str)}

if __name__ == '__main__':
    sample_data = {
        1: "one",
        2: "two",
        3: "three",
        4: 4,
        5: "five"
    }
    mapped_dict = map_dict_to_strings(sample_data)
    print(mapped_dict)