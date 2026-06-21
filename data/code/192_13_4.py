def find_common_items(list1, list2):
    if not all(isinstance(item, (list, set)) for item in [list1, list2]):
        raise ValueError("Both inputs must be either lists or sets.")
    
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    common_items = find_common_items(sample_list1, sample_list2)
    print(f"Intersection of {sample_list1} and {sample_list2}: {common_items}")
    
    sample_list3 = ['apple', 'banana', 'cherry']
    sample_list4 = ['banana', 'date', 'apple']
    common_items = find_common_items(sample_list3, sample_list4)
    print(f"Intersection of {sample_list3} and {sample_list4}: {common_items}")
    
    sample_set1 = {10, 20, 30}
    sample_set2 = {30, 10, 40}
    common_items = find_common_items(sample_set1, sample_set2)
    print(f"Intersection of {sample_set1} and {sample_set2}: {common_items}")