def _validate_index(idx):
    return isinstance(idx, int) and not isinstance(idx, bool)

def _check_bounds(index, length):
    return 0 <= index < length

def compare_elements_at_indices(list1, list2, indices):
    if not isinstance(list1, list):
        raise ValueError("list1 must be a list")
    if not isinstance(list2, list):
        raise ValueError("list2 must be a list")
    if not isinstance(indices, list):
        raise ValueError("indices must be a list")
    
    len1 = len(list1)
    len2 = len(list2)
    
    def compare_at(i):
        if not _validate_index(i):
            return False
        if not _check_bounds(i, len1) or not _check_bounds(i, len2):
            return False
        return list1[i] == list2[i]
    
    return [compare_at(idx) for idx in indices]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [10, 25, 30, 45, 60]
    sample_indices = [0, 1, 2, 3, 4, 5, -1, 10]
    result = compare_elements_at_indices(sample_list1, sample_list2, sample_indices)
    print(result)