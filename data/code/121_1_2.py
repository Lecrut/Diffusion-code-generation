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
    a = [1, 5, 3]
    b = [2, 4, 1]
    result1 = compare_quantities(a, b)
    print(result1)
    c = [10, 20]
    d = [5, 5]
    result2 = compare_quantities(c, d)
    print(result2)
    e = [1, 1, 1]
    f = [2, 2, 2]
    result3 = compare_quantities(e, f)
    print(result3)