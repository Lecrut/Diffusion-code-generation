def check_both_false(first: bool, second: bool) -> bool:
    return first is False and second is False

if __name__ == '__main__':
    val_a = False
    val_b = False
    outcome = check_both_false(val_a, val_b)
    print(outcome)
    val_c = True
    val_d = False
    outcome2 = check_both_false(val_c, val_d)
    print(outcome2)