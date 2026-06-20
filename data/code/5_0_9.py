def calculate_length_difference(first_length: str, second_length: str) -> float:
    try:
        value_one = float(first_length)
    except ValueError:
        raise ValueError(f"Invalid input for first length: '{first_length}' is not a number.")
    try:
        value_two = float(second_length)
    except ValueError:
        raise ValueError(f"Invalid input for second length: '{second_length}' is not a number.")
    return abs(value_one - value_two)
if __name__ == '__main__':
    result = calculate_length_difference('10.5', '5.3')
    print(result)