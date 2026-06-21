def remove_element(lst, item):
    return [x for x in lst if x != item]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    element_to_remove = 3
    result = remove_element(sample_list, element_to_remove)
    print(result)