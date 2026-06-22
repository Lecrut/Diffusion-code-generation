def check_conditions(x: float, y: float, z: float) -> bool:
    first_positive = x > 0.0
    second_smaller = y < x
    sum_match = z == (x + y)
    return first_positive and second_smaller and sum_match

if __name__ == '__main__':
    val_a = 3.5
    val_b = 1.2
    val_c = 4.7
    outcome = check_conditions(val_a, val_b, val_c)
    print(outcome)