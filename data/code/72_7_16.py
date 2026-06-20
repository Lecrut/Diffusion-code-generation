def compare_elements(list1, list2, index):
    try:
        element1 = list1[index]
        element2 = list2[index]
        return element1 <= element2
    except IndexError:
        raise ValueError("Index out of range for one or both lists")

if __name__ == '__main__':
    sample_list1 = [5, 3, 9, 8]
    sample_list2 = [4, 6, 7, 10]
    index_to_compare = 2
    result = compare_elements(sample_list1, sample_list2, index_to_compare)
    print(result)