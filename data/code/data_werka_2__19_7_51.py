def is_condition_true(a, b):
    return a == b

if __name__ == '__main__':
    sample_a = 42
    sample_b = 42
    result = is_condition_true(sample_a, sample_b)
    print(result)

    sample_c = "hello"
    sample_d = "world"
    result2 = is_condition_true(sample_c, sample_d)
    print(result2)