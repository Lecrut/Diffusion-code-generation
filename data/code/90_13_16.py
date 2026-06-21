def evaluate_threshold_or(first_value, second_value):
    if not isinstance(first_value, int) or not isinstance(second_value, int):
        raise ValueError("Inputs must be integers")
    return first_value > 10 or second_value > 10

if __name__ == '__main__':
    val_a = 15
    val_b = 8
    print(evaluate_threshold_or(val_a, val_b))