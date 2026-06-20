def compare_elements(list1, list2, index):
    if index < len(list1) and index < len(list2):
        return (list1[index], list2[index])
    else:
        raise IndexError("Index out of range")

if __name__ == '__main__':
    sample_list1 = [5, 3, 9, 1]
    sample_list2 = [4, 8, 7, 6]
    index_to_compare = 2
    result = compare_elements(sample_list1, sample_list2, index_to_compare)
    print(result)