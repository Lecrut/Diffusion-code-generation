def compare_sum_and_difference(value_one, value_two):
    if not isinstance(value_one, (int, float)) or isinstance(value_one, bool):
        raise ValueError("First argument must be a number")
    if not isinstance(value_two, (int, float)) or isinstance(value_two, bool):
        raise ValueError("Second argument must be a number")
    
    current_sum = value_one + value_two
    current_diff = value_one - value_two
    return current_sum > current_diff

if __name__ == '__main__':
    num_a = 100
    num_b = -50
    outcome = compare_sum_and_difference(num_a, num_b)
    print(outcome)