def remove_element(lst, element):
    return [x for x in lst if x != element]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5]
    element_to_remove = 2
    modified_list = remove_element(sample_list, element_to_remove)
    print(modified_list)