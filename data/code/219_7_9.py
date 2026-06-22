def validate_lists(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise ValueError("Both inputs must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length.")

def max_pairs(list1, list2):
    validate_lists(list1, list2)
    return [max(a, b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [4, 6, 8]
    sample_list2 = [3, 9, 7]
    print(max_pairs(sample_list1, sample_list2))