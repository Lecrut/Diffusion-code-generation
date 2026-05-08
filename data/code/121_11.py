def compare_quantities_size(a, b):
    size_a = len(a)
    size_b = len(b)
    if size_a > size_b:
        return (1, 0)
    elif size_b > size_a:
        return (0, 1)
    else:
        return (0, 0)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [5, 6]
    print(compare_quantities_size(list1, list2))
    list3 = (10, 20)
    list4 = (30, 40, 50)
    print(compare_quantities_size(list3, list4))
    list5 = [1, 2]
    list6 = [3, 4]
    print(compare_quantities_size(list5, list6))
    list7 = [1, 2, 3]
    list8 = [4, 5, 6]
    print(compare_quantities_size(list7, list8))