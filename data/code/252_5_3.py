def compare_list_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    return sum1 == sum2
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7, 8]
    result = compare_list_sums(list_a, list_b)
    print(result)
    list_c = [10, 20]
    list_d = [15, 5]
    result2 = compare_list_sums(list_c, list_d)
    print(result2)