def is_condition_true(a, b):
    return a == b

if __name__ == '__main__':
    SAMPLE_A = 42
    SAMPLE_B = 42
    result = is_condition_true(SAMPLE_A, SAMPLE_B)
    print(result)

    SAMPLE_C = "hello"
    SAMPLE_D = "world"
    try:
        result2 = is_condition_true(SAMPLE_C, SAMPLE_D)
        print(result2)
    except ValueError as e:
        print(e)