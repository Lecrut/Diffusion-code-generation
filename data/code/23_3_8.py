def compare_sums_and_lists(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    sum_difference = sum_a - sum_b
    list_difference = abs(len(list_a) - len(list_b))
    list_element_difference = sum(abs(x - y) for x, y in zip(list_a, list_b))
    return sum_difference, list_element_difference, list_difference
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    diff1, diff2, diff3 = compare_sums_and_lists(list1, list2)
    print(f"Sum difference (list_a - list_b): {diff1}")
    print(f"Absolute difference between lists (based on length): {diff3}")
    print(f"Sum of absolute differences between corresponding elements: {diff2}")