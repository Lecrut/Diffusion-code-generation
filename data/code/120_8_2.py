def compare_numbers(a, b):
    result_equal = a == b
    result_not_equal = a != b
    return (result_equal, result_not_equal)
if __name__ == '__main__':
    a_val = 5
    b_val = 10
    result = compare_numbers(a_val, b_val)
    print(result)