def is_condition_true(a, b):
    EQUALITY_THRESHOLD = 0.00001
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) < EQUALITY_THRESHOLD
    else:
        return a == b

if __name__ == '__main__':
    sample_a = 42.00001
    sample_b = 42.00002
    result = is_condition_true(sample_a, sample_b)
    print(result)