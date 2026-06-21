def are_floats_near_equal(a, b, tolerance=1e-9):
    return abs(a - b) <= tolerance

if __name__ == '__main__':
    sample_a = 0.1 + 0.2
    sample_b = 0.3
    print(are_floats_near_equal(sample_a, sample_b))