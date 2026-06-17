def compare_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    return abs(sum1 - sum2)
if __name__ == '__main__':
    list_a = [1, 5, 10]
    list_b = [3, 7, 2]
    print(compare_sums(list_a, list_b))
    list_c = [100, 200]
    list_d = []
    print(compare_sums(list_c, list_d))
    list_e = [5, 5]
    list_f = [5, 5]
    print(compare_sums(list_e, list_f))