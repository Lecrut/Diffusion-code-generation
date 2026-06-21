def filter_element(lst, element):
    return [item for item in lst if item != element]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    element_to_remove = 30
    filtered_list = filter_element(sample_list, element_to_remove)
    print(filtered_list)