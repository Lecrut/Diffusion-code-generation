def test_or_condition(a, b):
    result = a or b
    return result

if __name__ == '__main__':
    sample_a = 0
    sample_b = 42
    output = test_or_condition(sample_a, sample_b)
    print(output)