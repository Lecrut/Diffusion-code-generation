def compare_sums_and_lists(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    sum_difference = sum_a - sum_b
    list_difference = abs(len(list_a) - len(list_b))
    list_content_difference = sum(abs(x - y) for x, y in zip(list_a, list_b))
    return sum_difference, list_content_difference, list_difference
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50]
    result = compare_sums_and_lists(list1, list2)
    print(result)