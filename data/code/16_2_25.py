def is_positive(x):
    return x > 0

if __name__ == '__main__':
    sample_values = [1, -2, 0, 3.5, -0.1]
    for value in sample_values:
        print(f"is_positive({value}): {is_positive(value)}")