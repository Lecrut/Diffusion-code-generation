def compare_quantities_size(a, b):
    size_a = len(a)
    size_b = len(b)
    if size_a > size_b:
        return (1, 0)
    elif size_b > size_a:
        return (0, 1)
    else:
        return (1, 1)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [5, 6]
    result1 = compare_quantities_size(list1, list2)
    print(result1)
    list3 = (10, 20, 30)
    list4 = (40, 50, 60)
    result2 = compare_quantities_size(list3, list4)
    print(result2)
    list5 = [1, 2]
    list6 = [3, 4]
    result3 = compare_quantities_size(list5, list6)
    print(result3)
    list7 = [1, 2, 3]
    list8 = [4, 5, 6]
    result4 = compare_quantities_size(list7, list8)
    print(result4)
    list9 = [1, 2]
    list10 = [3, 4]
    result5 = compare_quantities_size(list9, list10)
    print(result5)