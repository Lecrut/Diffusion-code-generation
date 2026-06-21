def filter_string(input_list, string_to_remove):
    if not isinstance(input_list, list) or not all(isinstance(item, str) for item in input_list):
        raise ValueError("Input must be a list of strings")
    if not isinstance(string_to_remove, str):
        raise ValueError("String to remove must be a string")
    
    return [item for item in input_list if item != string_to_remove]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date", "banana"]
    filtered_list = filter_string(sample_list, "banana")
    print(filtered_list)