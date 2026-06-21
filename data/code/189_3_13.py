def filter_element(original_list, element_to_remove):
    return [item for item in original_list if item != element_to_remove]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3]
    element_to_filter = 3
    result = filter_element(sample_list, element_to_filter)
    print(result)