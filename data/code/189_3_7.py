def filter_element(input_list, element_to_remove):
    return list(item for item in input_list if item != element_to_remove)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    element_to_remove = 3
    filtered_list = filter_element(sample_list, element_to_remove)
    print(filtered_list)