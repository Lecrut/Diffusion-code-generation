def is_positive_and_less_than_100(value: int) -> bool:
    try:
        if value < 0 or value >= 100:
            raise ValueError("Value must be positive and less than 100")
        return True
    except TypeError as e:
        print(f"Invalid input type: {e}")
        return False

if __name__ == '__main__':
    test_values = [50, -5, 100, '100']
    for value in test_values:
        result = is_positive_and_less_than_100(value)
        print(f"is_positive_and_less_than_100({value}) is: {result}")