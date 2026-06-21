def is_zero(value):
    return value == 0

if __name__ == '__main__':
    sample_values = [0, 1, -0.0, 0.001, 1e-308, '0', None, True, False]
    for val in sample_values:
        print(f"is_zero({val}): {is_zero(val)}")