def are_strictly_true(a, b):
    return bool(a) and bool(b)

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = are_strictly_true(sample_a, sample_b)
    print(result)