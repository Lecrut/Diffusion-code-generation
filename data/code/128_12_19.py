def is_negative(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [-1, 0, 1, -3.14, 2.718]
    for value in sample_values:
        result = is_negative(value)
        print(f"Value: {value}, Is Negative: {result}")