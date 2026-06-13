def compare_quantities(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 > sum2:
        larger_list = "list1"
        difference = sum1 - sum2
    elif sum2 > sum1:
        larger_list = "list2"
        difference = sum2 - sum1
    else:
        larger_list = "Equal"
        difference = 0
    return {
        "larger_sum_list": larger_list,
        "difference": difference
    }
if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 15, 25]
    result1 = compare_quantities(list_a, list_b)
    print(result1)
    list_c = [1, 2, 3]
    list_d = [4, 5, 6]
    result2 = compare_quantities(list_c, list_d)
    print(result2)
    list_e = [100, 50]
    list_f = [70, 80]
    result3 = compare_quantities(list_e, list_f)
    print(result3)