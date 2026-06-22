def evaluate_greater(x, y):
    is_greater = x > y
    return is_greater

if __name__ == '__main__':
    first_value = 42
    second_value = 10
    comparison_result = evaluate_greater(first_value, second_value)
    print(comparison_result)