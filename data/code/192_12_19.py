def find_common_elements(list1, list2):
    if not all(isinstance(item, int) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers")
    
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return sorted(intersection)

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    sample_list2 = [0, 2, 4, 6, 8, 7, 9]
    print(find_common_elements(sample_list1, sample_list2))