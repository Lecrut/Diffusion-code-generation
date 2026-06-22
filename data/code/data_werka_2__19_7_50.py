def is_condition_true(a, b):
    comparison_result = (a == b)
    return comparison_result

if __name__ == '__main__':
    sample_a = 3.14
    sample_b = 3.14
    result = is_condition_true(sample_a, sample_b)
    print(result)