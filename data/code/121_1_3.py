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
    list_a = [1, 5, 3, 7]
    list_b = [2, 4, 1, 6]
    result = compare_quantities(list_a, list_b)
    print(result)
    list_c = [10, 20]
    list_d = [5, 5]
    result2 = compare_quantities(list_c, list_d)
    print(result2)
    list_e = [1, 2, 3]
    list_f = [1, 2, 3]
    result3 = compare_quantities(list_e, list_f)
    print(result3)