def check_negativity(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [10.5, -3.2, 0.0, -999.99, 42.0]
    for val in sample_values:
        result = check_negativity(val)
        print(f"Value: {val}, Is Negative: {result}")