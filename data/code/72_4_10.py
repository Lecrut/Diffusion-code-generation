def merge_lists_at_index(list1, list2, index):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists")
    
    if not isinstance(index, int) or index < 0:
        raise IndexError("Index must be a non-negative integer")
    
    if index >= len(list1) or index >= len(list2):
        raise IndexError("Index out of bounds for one of the lists")
    
    return [(list1[index], list2[index])]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    sample_index = 1
    print(merge_lists_at_index(sample_list1, sample_list2, sample_index))