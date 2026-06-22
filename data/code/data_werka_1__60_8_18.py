def get_last_item(strings_list):
    if not isinstance(strings_list, list) or not strings_list:
        raise ValueError("Input must be a non-empty list of strings.")
    
    for item in strings_list:
        if not isinstance(item, str):
            raise ValueError("All elements in the list must be strings.")
    
    return strings_list[-1]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    print(f"List: {sample_list}")
    last_item = get_last_item(sample_list)
    print(f"Last item: {last_item}")