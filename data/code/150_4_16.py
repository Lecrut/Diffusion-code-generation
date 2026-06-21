def filter_string(input_list, value_to_remove):
    if not isinstance(input_list, list) or not all(isinstance(item, str) for item in input_list):
        raise ValueError("Input must be a list of strings")
    return [item for item in input_list if item != value_to_remove]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "apple"]
    filtered_list = filter_string(sample_list, "apple")
    print(filtered_list)