def filter_element(lst, element):
    return [x for x in lst if x != element]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3]
    element_to_remove = 3
    filtered_list = filter_element(sample_list, element_to_remove)
    print(filtered_list)