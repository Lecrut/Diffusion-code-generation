def compare_booleans(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    return [a == b]

if __name__ == '__main__':
    list1 = [True, False]
    try:
        result1 = compare_booleans(list1[0], list1[1])
        print(result1)
    except ValueError as e:
        print(e)

    list2 = [True, True]
    try:
        result2 = compare_booleans(list2[0], list2[1])
        print(result2)
    except ValueError as e:
        print(e)

    list3 = [False, True]
    try:
        result3 = compare_booleans(list3[0], list3[1])
        print(result3)
    except ValueError as e:
        print(e)