def compare_list_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    comparison_result = "equal" if sum1 == sum2 else ("list1 is greater" if sum1 > sum2 else "list2 is greater")
    print(f"Sum of list1: {sum1}")
    print(f"Sum of list2: {sum2}")
    print(f"Comparison result: {comparison_result}")
if __name__ == '__main__':
    list_a = [1, 5, 3, 7]
    list_b = [2, 4, 6, 1]
    compare_list_sums(list_a, list_b)