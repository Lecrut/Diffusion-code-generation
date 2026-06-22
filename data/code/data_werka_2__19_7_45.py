def is_condition_true(a, b):
    if not isinstance(a, type(b)):
        raise ValueError("Inputs must be of the same type")
    return a == b

if __name__ == '__main__':
    sample_a = "hello"
    sample_b = "hello"
    try:
        result = is_condition_true(sample_a, sample_b)
        print(result)
    except ValueError as e:
        print(e)