def sum_digits(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Expected a numeric type")
    if isinstance(value, float) and not value.is_integer():
        raise ValueError("Input must be an integer")
    return sum(map(int, str(int(abs(value)))))

if __name__ == '__main__':
    sample_number = 123456
    total = sum_digits(sample_number)
    print(total)