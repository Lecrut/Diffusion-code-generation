def combine_lists(list1, list2):
    combined = set(list1)
    combined.update(list2)
    return list(combined)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result1 = combine_lists(list_a, list_b)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Combined List (no duplicates): {result1}")
    list_c = ['apple', 'banana', 'cherry']
    list_d = ['cherry', 'date', 'elderberry']
    result2 = combine_lists(list_c, list_d)
    print(f"List C: {list_c}")
    print(f"List D: {list_d}")
    print(f"Combined List (no duplicates): {result2}")