def reverse_lists(list1, list2):
    if not all(isinstance(lst, list) for lst in [list1, list2]):
        raise ValueError("Both inputs must be lists.")
    
    return list(reversed(list1)) + list(reversed(list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = reverse_lists(sample_list1, sample_list2)
    print("Reversed lists:", result)