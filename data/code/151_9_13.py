def merge_sets(list1, list2):
    if not all(isinstance(subset, set) for subset in list1 + list2):
        raise ValueError("All elements must be sets")
    
    return set().union(*list1, *list2)

if __name__ == '__main__':
    sample_list1 = [{1, 2}, {3, 4}]
    sample_list2 = [{4, 5}, {6, 7}]
    result = merge_sets(sample_list1, sample_list2)
    print(result)