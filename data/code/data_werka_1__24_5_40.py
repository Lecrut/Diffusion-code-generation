def is_strictly_less_than_zero(x):
    return x < 0

if __name__ == '__main__':
    sample_values = [0.0, -1e-308, 1e-308, -0.5, 0.5, -1.0, 1.0]
    for value in sample_values:
        print(f"{value}: {is_strictly_less_than_zero(value)}")