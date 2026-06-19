def is_positive(x):
    return x > 0

if __name__ == '__main__':
    test_values = [10, -5, 0, 3.14, -0.001]
    for value in test_values:
        result = is_positive(value)
        print(f"{value} is positive: {result}")