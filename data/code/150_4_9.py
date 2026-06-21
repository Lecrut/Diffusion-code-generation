def remove_value(input_list, value_to_remove):
    if not isinstance(input_list, list) or not all(isinstance(item, str) for item in input_list):
        raise ValueError("input_list must be a list of strings")
    if not isinstance(value_to_remove, str):
        raise ValueError("value_to_remove must be a string")
    
    return [item for item in input_list if item != value_to_remove]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'apple']
    value_to_remove = 'apple'
    result_list = remove_value(sample_list, value_to_remove)
    print(result_list)