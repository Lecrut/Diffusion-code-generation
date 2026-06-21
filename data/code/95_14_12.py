def check_conditions(first: float, second: float, third: float) -> bool:
    is_positive = first > 0.0
    is_less_than_first = second < first
    is_sum = third == (first + second)
    return is_positive and is_less_than_first and is_sum

if __name__ == '__main__':
    val_a = 3.14
    val_b = 1.14
    val_c = 4.28
    outcome = check_conditions(val_a, val_b, val_c)
    print(outcome)