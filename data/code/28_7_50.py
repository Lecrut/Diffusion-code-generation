def is_larger(a, b):
    result = (a > b)
    return result

if __name__ == '__main__':
    value1 = 7
    value2 = 3
    print(is_larger(value1, value2))

    sample_a = -5
    sample_b = -10
    print(is_larger(sample_a, sample_b))

    test_value_1 = 0.5
    test_value_2 = 0.5
    print(is_larger(test_value_1, test_value_2))