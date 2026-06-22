NUMERIC_THRESHOLD = 0

def compare_sum_and_difference(first_value, second_value):
    total = first_value + second_value
    difference = first_value - second_value
    return total > difference

if __name__ == '__main__':
    val_one = 15
    val_two = 2
    outcome = compare_sum_and_difference(val_one, val_two)
    print(outcome)