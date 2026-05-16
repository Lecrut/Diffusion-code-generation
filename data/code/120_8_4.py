def compare_numbers(a, b):
    result_equal = a == b
    result_not_equal = a != b
    return (result_equal, result_not_equal)
if __name__ == '__main__':
    val1 = 5
    val2 = 5
    result1 = compare_numbers(val1, val2)
    print(result1)
    val3 = 10
    val4 = 3
    result2 = compare_numbers(val3, val4)
    print(result2)