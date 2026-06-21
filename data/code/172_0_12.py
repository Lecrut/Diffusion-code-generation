def map_dict_values(input_dict):
    if not isinstance(input_dict, dict) or not all(isinstance(k, int) and isinstance(v, str) for k, v in input_dict.items()):
        raise ValueError("Input must be a dictionary with integer keys and string values")
    
    return {k: v for k, v in input_dict.items()}

if __name__ == '__main__':
    sample_data = {
        1: "apple",
        2: "zebra",
        3: "banana",
        4: "cat",
        5: "dog"
    }
    mapped_values = map_dict_values(sample_data)
    print(mapped_values)