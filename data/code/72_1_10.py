def compare_elements(list1, list2, index):
    if index < len(list1) and index < len(list2):
        return (list1[index], list2[index])
    else:
        raise IndexError("Index out of bounds")

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [5, 15, 25]
    index_to_compare = 1
    result = compare_elements(sample_list1, sample_list2, index_to_compare)
    print(result)