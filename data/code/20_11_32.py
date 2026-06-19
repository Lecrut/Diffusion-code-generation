def compare_items(a, b):
    if type(a) is not type(b):
        return False
    return a == b
if __name__ == '__main__':
    result1 = compare_items(5, 5)
    print(result1)
    result2 = compare_items(5, '5')
    print(result2)
    result3 = compare_items([1, 2, 3], [1, 2, 3])
    print(result3)
    result4 = compare_items((1, 2), (1, 2))
    print(result4)
    result5 = compare_items({'a': 1}, {'a': 1})
    print(result5)