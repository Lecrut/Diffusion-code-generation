def compare_sums(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    return abs(sum1 - sum2)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7]
    print(compare_sums(list_a, list_b))
    list_c = [10, 20]
    list_d = []
    print(compare_sums(list_c, list_d))
    list_e = []
    list_f = []
    print(compare_sums(list_e, list_f))