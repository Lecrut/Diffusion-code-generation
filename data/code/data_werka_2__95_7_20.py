def verify_conditions(first, second, third):
    is_positive = first > 0
    is_even = second % 2 == 0
    product = first * second
    is_divisible = third % product == 0 if product != 0 else False
    return is_positive and is_even and is_divisible

if __name__ == '__main__':
    val_a = 3
    val_b = 6
    val_c = 18
    outcome = verify_conditions(val_a, val_b, val_c)
    print(outcome)