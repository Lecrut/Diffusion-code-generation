def is_condition_true(a, b):
    if not isinstance(a, type(b)):
        raise ValueError("Inputs must be of the same type")
    return a == b

if __name__ == '__main__':
    try:
        sample_a = 42
        sample_b = 42
        result1 = is_condition_true(sample_a, sample_b)
        print(result1)

        sample_c = "hello"
        sample_d = "world"
        result2 = is_condition_true(sample_c, sample_d)
        print(result2)

        sample_e = [1, 2, 3]
        sample_f = [1, 2, 3]
        result3 = is_condition_true(sample_e, sample_f)
        print(result3)

    except ValueError as e:
        print(e)