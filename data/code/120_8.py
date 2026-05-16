def compare_numbers(a, b):
    result_equal = a == b
    result_not_equal = a != b
    return (result_equal, result_not_equal)
if __name__ == '__main__':
    x = 5
    y = 5
    result1 = compare_numbers(x, y)
    print(result1)
    x = 10
    y = 3
    result2 = compare_numbers(x, y)
    print(result2)