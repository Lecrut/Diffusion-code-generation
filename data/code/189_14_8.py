def remove_element_by_reference(lst, element):
    if element in lst:
        lst.remove(element)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    element_to_remove = 3
    remove_element_by_reference(sample_list, element_to_remove)
    print(sample_list)