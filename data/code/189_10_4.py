def remove_element(lst, element):
    return [item for item in lst if item != element]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5]
    element_to_remove = 2
    modified_list = remove_element(sample_list, element_to_remove)
    print(modified_list)