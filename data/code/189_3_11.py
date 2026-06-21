def filter_element(lst, element):
    if not isinstance(lst, list) or not all(isinstance(item, (int, float)) for item in lst):
        raise ValueError("Input must be a list of numbers.")
    
    return [item for item in lst if item != element]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3]
    element_to_filter = 3
    filtered_list = filter_element(sample_list, element_to_filter)
    print(filtered_list)