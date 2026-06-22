def validate_positive_integer(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")
    return value

def evaluate_or_greater_than_ten(num_one, num_two):
    validated_first = validate_positive_integer(num_one)
    validated_second = validate_positive_integer(num_two)
    return validated_first > 10 or validated_second > 10

if __name__ == '__main__':
    first_val = 15
    second_val = 4
    result = evaluate_or_greater_than_ten(first_val, second_val)
    print(result)