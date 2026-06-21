def is_condition_true(a, b):
    def validate_inputs(x, y):
        if type(x) != type(y):
            raise ValueError("Inputs must be of the same type")

    try:
        validate_inputs(a, b)
        return a == b
    except ValueError as e:
        print(e)
        return False

if __name__ == '__main__':
    sample_a = 42
    sample_b = 42
    result1 = is_condition_true(sample_a, sample_b)
    print(result1)

    sample_c = "hello"
    sample_d = "world"
    result2 = is_condition_true(sample_c, sample_d)
    print(result2)