def merge_lists_at_index(list1, list2, index):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(list1) or index >= len(list2):
        raise IndexError("Index out of range for the given lists")

    return [(list1[index], list2[index])]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    sample_index = 1
    try:
        result = merge_lists_at_index(sample_list1, sample_list2, sample_index)
        print(result)
    except Exception as e:
        print(e)