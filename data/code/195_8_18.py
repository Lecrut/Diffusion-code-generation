def compare_lists_by_index(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length")
    
    differing_pairs = []
    for index, (value1, value2) in enumerate(zip(list1, list2)):
        if value1 != value2:
            differing_pairs.append((index, value1, value2))
    
    return differing_pairs

if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 5, 4]
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    result1 = compare_lists_by_index(list_a, list_b)
    print(f"Differing pairs (A vs B): {result1}")

    list_c = [1, 2, 3]
    list_d = [4, 5, 6]
    print("\nList C: ", list_c)
    print("List D: ", list_d)
    result2 = compare_lists_by_index(list_c, list_d)
    print(f"Differing pairs (C vs D): {result2}")