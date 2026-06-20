def is_positive_and_less_than_100(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or float")
    return value > 0 and value < 100

if __name__ == '__main__':
    sample_values = [50, -10, 100, 0.5, 'abc']
    for value in sample_values:
        try:
            result = is_positive_and_less_than_100(value)
            print(f"is_positive_and_less_than_100({value}) is: {result}")
        except ValueError as e:
            print(e)