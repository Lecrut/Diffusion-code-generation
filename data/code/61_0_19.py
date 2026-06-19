def fetch_element_from_list(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        return "Index out of bounds"

if __name__ == '__main__':
    example_list = [5, 15, 25, 35, 45]
    valid_index = 3
    invalid_index = 7
    
    element_valid = fetch_element_from_list(example_list, valid_index)
    element_invalid = fetch_element_from_list(example_list, invalid_index)
    
    print(f"List: {example_list}")
    print(f"Element at index {valid_index}: {element_valid}")
    print(f"Element at index {invalid_index}: {element_invalid}")