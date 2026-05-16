def compare_quantities(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1 > sum2:
        return (list1, "list1")
    elif sum2 > sum1:
        return (list2, "list2")
    else:
        return (list1, "equal")
if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 15, 25]
    result1 = compare_quantities(list_a, list_b)
    print(result1)
    list_c = [1, 2, 3]
    list_d = [100, 200]
    result2 = compare_quantities(list_c, list_d)
    print(result2)
    list_e = [50, 50]
    list_f = [10, 10]
    result3 = compare_quantities(list_e, list_f)
    print(result3)