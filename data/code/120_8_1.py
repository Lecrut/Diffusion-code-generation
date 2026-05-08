def compare_numbers(a, b):
    result_equal = a == b
    result_not_equal = a != b
    return (result_equal, result_not_equal)
if __name__ == '__main__':
    x = 5
    y = 10
    print(compare_numbers(x, y))
    x = 5
    y = 5
    print(compare_numbers(x, y))
    x = 3
    y = 7
    print(compare_numbers(x, y))