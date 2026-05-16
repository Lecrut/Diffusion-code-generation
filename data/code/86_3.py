def compare_booleans(a, b):
    return [a == b]
if __name__ == '__main__':
    list1 = [True, False]
    result1 = compare_booleans(list1[0], list1[1])
    print(result1)
    list2 = [True, True]
    result2 = compare_booleans(list2[0], list2[1])
    print(result2)
    list3 = [False, True]
    result3 = compare_booleans(list3[0], list3[1])
    print(result3)