def check_both_false(a: bool, b: bool) -> bool:
    mask_a = int(a)
    mask_b = int(b)
    combined = mask_a | mask_b
    return combined == 0

if __name__ == '__main__':
    val_a = True
    val_b = False
    outcome = check_both_false(val_a, val_b)
    print(outcome)
    val_x = False
    val_y = False
    result = check_both_false(val_x, val_y)
    print(result)