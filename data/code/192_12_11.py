def find_common_elements(list1, list2):
    try:
        set1 = set(list1)
        set2 = set(list2)
        if not all(isinstance(item, int) for item in set1.union(set2)):
            raise ValueError("Both inputs must be lists of integers.")
        intersection = set1 & set2
        return sorted(intersection)
    except TypeError:
        raise ValueError("Inputs must be lists.")

if __name__ == '__main__':
    sample_list1 = [1, 3, 5, 7, 9]
    sample_list2 = [0, 2, 4, 6, 8, 7, 9]
    print(find_common_elements(sample_list1, sample_list2))