def is_negative(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [20, -15, 0, -3.14]
    for value in sample_values:
        result = is_negative(value)
        print(f"Value: {value}, Is Negative: {result}")