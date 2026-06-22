def validate_positive_integer(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")
    return value

def evaluate_greater_than_ten_or(a, b):
    valid_a = validate_positive_integer(a)
    valid_b = validate_positive_integer(b)
    condition_one = valid_a > 10
    condition_two = valid_b > 10
    return condition_one or condition_two

if __name__ == '__main__':
    num_x = 4
    num_y = 11
    is_condition_met = evaluate_greater_than_ten_or(num_x, num_y)
    print(is_condition_met)