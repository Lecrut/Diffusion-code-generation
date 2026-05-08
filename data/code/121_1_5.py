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
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    print(compare_quantities(a, b))
    c = [10, 20]
    d = [5, 5]
    print(compare_quantities(c, d))
    e = [1, 1, 1]
    f = [2, 2, 2]
    print(compare_quantities(e, f))