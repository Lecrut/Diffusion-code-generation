def evaluate_or_greater_than_ten(first_value, second_value):
    if first_value > 10:
        return True
    return second_value > 10

if __name__ == '__main__':
    val_one = 15
    val_two = 8
    outcome = evaluate_or_greater_than_ten(val_one, val_two)
    print(outcome)