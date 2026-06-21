def compare_lists(list_a, list_b):
    return set(list_a) == set(list_b), sorted(set(list_a) ^ set(list_b))

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [4, 3, 2, 1]
    result1 = compare_lists(list1, list2)
    print(f"Comparing {list1} and {list2}: Equality={result1[0]}, Differing Elements={result1[1]}")