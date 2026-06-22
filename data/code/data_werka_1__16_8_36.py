def is_positive_number(value):
    try:
        number = int(value)
        return number > 0
    except ValueError:
        return False

if __name__ == '__main__':
    sample_values = [10, -5, 'abc', 0, 23]
    for value in sample_values:
        result = is_positive_number(value)
        print(f"Is {value} positive? {result}")