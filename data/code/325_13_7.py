def compare_list_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    result = sum1 + sum2
    print(f"Sum of the first list: {sum1}")
    print(f"Sum of the second list: {sum2}")
    print(f"The sum of both lists is: {result}")
if __name__ == '__main__':
    list_a = [1, 5, 10, 15]
    list_b = [2, 4, 6, 8]
    compare_list_sums(list_a, list_b)