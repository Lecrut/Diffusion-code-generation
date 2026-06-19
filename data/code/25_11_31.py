def is_zero(x):
    return x == 0

if __name__ == '__main__':
    sample_values = [0, -1, 5, 0.0, None]
    for value in sample_values:
        print(f"{value}: {is_zero(value)}")