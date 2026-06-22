def evaluate_conditions(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    val_a = False
    val_b = False
    outcome = evaluate_conditions(val_a, val_b)
    print(outcome)