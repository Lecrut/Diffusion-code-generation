def compare_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length")
    
    diff_pairs = []
    for index, (value1, value2) in enumerate(zip(list1, list2)):
        if value1 != value2:
            diff_pairs.append((index, value1, value2))
    
    return diff_pairs

if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 5, 4]
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    result1 = compare_lists(list_a, list_b)
    print(f"Difference pairs (A vs B): {result1}")
    
    list_c = [5, 6, 7]
    list_d = [5, 6, 8]
    print(f"\nList C: {list_c}")
    print(f"List D: {list_d}")
    result2 = compare_lists(list_c, list_d)
    print(f"Difference pairs (C vs D): {result2}")