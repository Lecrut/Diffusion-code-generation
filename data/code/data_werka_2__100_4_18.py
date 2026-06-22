def evaluate_greater_than(x, y):
    difference = x - y
    is_positive = difference > 0
    return is_positive

if __name__ == '__main__':
    first_value = 100
    second_value = 42
    comparison_result = evaluate_greater_than(first_value, second_value)
    print(comparison_result)