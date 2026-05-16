def compare_quantities_size(a, b):
    size_a = len(a)
    size_b = len(b)
    if size_a > size_b:
        return (a, "greater")
    elif size_b > size_a:
        return (b, "greater")
    else:
        return (a, "equal")
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7, 8]
    list4 = [9]
    result1 = compare_quantities_size(list1, list2)
    print(result1)
    result2 = compare_quantities_size(list3, list4)
    print(result2)
    result3 = compare_quantities_size(list1, list3)
    print(result3)
    result4 = compare_quantities_size(list2, list2)
    print(result4)