def compare_sum_and_difference(num_one, num_two):
    if not isinstance(num_one, (int, float)) or not isinstance(num_two, (int, float)):
        raise ValueError("Both inputs must be numbers")
    if isinstance(num_one, bool) or isinstance(num_two, bool):
        raise ValueError("Booleans are not valid numeric inputs")
    total = num_one + num_two
    gap = num_one - num_two
    return total > gap

if __name__ == '__main__':
    val_x = 20
    val_y = 8
    outcome = compare_sum_and_difference(val_x, val_y)
    print(outcome)