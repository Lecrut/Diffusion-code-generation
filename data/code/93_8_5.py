def are_both_false(first: bool, second: bool) -> bool:
    if first:
        return False
    if second:
        return False
    return True

if __name__ == '__main__':
    val_a = False
    val_b = False
    outcome = are_both_false(val_a, val_b)
    print(outcome)