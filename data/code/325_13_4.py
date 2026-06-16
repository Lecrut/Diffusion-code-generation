def compare_list_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    comparison_result = sum1 - sum2
    print(f"Sum of the first list: {sum1}")
    print(f"Sum of the second list: {sum2}")
    print(f"Difference (List 1 Sum - List 2 Sum): {comparison_result}")
if __name__ == '__main__':
    list_a = [1, 5, 3, 7]
    list_b = [2, 4, 6, 8]
    compare_list_sums(list_a, list_b)