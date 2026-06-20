def are_strictly_true(value1, value2):
    return bool(value1) and bool(value2)

if __name__ == '__main__':
    sample_a = 10
    sample_b = 0
    result = are_strictly_true(sample_a, sample_b)
    print(result)