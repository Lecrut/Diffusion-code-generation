def is_hashable(item):
    try:
        hash(item)
        return True
    except TypeError:
        return False

def unique_common_items(list1, list2):
    if not all(is_hashable(item) for item in list1 + list2):
        raise ValueError("Both lists must contain only hashable elements")
    
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(unique_common_items(sample_list1, sample_list2))