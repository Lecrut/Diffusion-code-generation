def check_difference(a, b):
    return not (a == b)

if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 42.0
    result = check_difference(sample_value1, sample_value2)
    print(result)