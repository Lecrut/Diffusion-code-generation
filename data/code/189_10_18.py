def remove_element(lst, element):
    while element in lst:
        lst.remove(element)
    return lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 3, 5]
    element_to_remove = 3
    modified_list = remove_element(sample_list, element_to_remove)
    print(modified_list)