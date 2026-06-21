def remove_element(lst, item):
    if item in lst:
        lst.remove(item)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    element_to_remove = 3
    remove_element(sample_list, element_to_remove)
    print(sample_list)