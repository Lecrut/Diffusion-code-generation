def check_both_false(boolean_a: bool, boolean_b: bool) -> bool:
    if boolean_a or boolean_b:
        return False
    return True

if __name__ == '__main__':
    val_a = False
    val_b = False
    outcome = check_both_false(val_a, val_b)
    print(outcome)