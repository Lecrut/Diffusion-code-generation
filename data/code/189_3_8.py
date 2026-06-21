def filter_element(lst, element):
    return list(item for item in lst if item != element)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2]
    element_to_remove = 2
    filtered_list = filter_element(sample_list, element_to_remove)
    print(filtered_list)