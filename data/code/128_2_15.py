def is_negative(num):
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a float or int")
    return num < 0

if __name__ == '__main__':
    sample_values = [10.5, -3.2, 0, -100, 3.14]
    for value in sample_values:
        result = is_negative(value)
        print(f"Value: {value}, Is Negative: {result}")