def check_conditions(first: float, second: float, third: float) -> bool:
    MINIMUM_THRESHOLD = 0.0
    return first > MINIMUM_THRESHOLD and second < first and third == first + second

if __name__ == '__main__':
    val_a = 10.0
    val_b = 3.0
    val_c = 13.0
    outcome = check_conditions(val_a, val_b, val_c)
    print(outcome)