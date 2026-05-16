def compare_sums_and_lists(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    sum_difference = sum_a - sum_b
    list_difference = abs(len(list_a) - len(list_b)) + sum(abs(x - y) for x, y in zip(list_a, list_b))
    return sum_difference, list_difference
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    diff1, diff2 = compare_sums_and_lists(list1, list2)
    print(f"List A: {list1}")
    print(f"List B: {list2}")
    print(f"Difference between sums (Sum(A) - Sum(B)): {diff1}")
    print(f"Absolute difference between lists (Length difference + Sum of absolute element differences): {diff2}")