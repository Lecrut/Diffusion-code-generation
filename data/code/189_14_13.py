def remove_by_reference(lst, element):
    if element in lst:
        lst.remove(element)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Original list:", sample_list)
    remove_by_reference(sample_list, 3)
    print("Modified list:", sample_list)