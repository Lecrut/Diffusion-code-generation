def is_condition_true(a, b):
    if a is b:
        return True
    if type(a) != type(b):
        return False
    return a == b

if __name__ == '__main__':
    sample_a = 42
    sample_b = 42
    result = is_condition_true(sample_a, sample_b)
    print(result)

    sample_c = "hello"
    sample_d = "world"
    result = is_condition_true(sample_c, sample_d)
    print(result)