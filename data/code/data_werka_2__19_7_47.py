def is_condition_true(a, b):
    try:
        return a == b
    except Exception as e:
        raise ValueError(f'Comparison failed: {e}')
if __name__ == '__main__':
    sample_a = 42
    sample_b = 42
    try:
        result1 = is_condition_true(sample_a, sample_b)
        print(result1)
    except ValueError as e:
        print(e)
    sample_c = 'hello'
    sample_d = 'world'
    try:
        result2 = is_condition_true(sample_c, sample_d)
        print(result2)
    except ValueError as e:
        print(e)
    sample_e = [1, 2, 3]
    sample_f = (1, 2, 3)
    try:
        result3 = is_condition_true(sample_e, sample_f)
        print(result3)
    except ValueError as e:
        print(e)