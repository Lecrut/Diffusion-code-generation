def remove_element(lst, element):
    if not isinstance(lst, list) or not all(isinstance(item, (int, float)) for item in lst):
        raise ValueError("Input must be a list of numbers")
    if not isinstance(element, (int, float)):
        raise ValueError("Element to remove must be a number")

    result = []
    for item in lst:
        if item != element:
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 20]
    element_to_remove = 20
    modified_list = remove_element(sample_list, element_to_remove)
    print(modified_list)