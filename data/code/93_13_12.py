def check_both_false(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Arguments must be of type bool")
    return not (a ^ b) and not a

if __name__ == '__main__':
    val_a = False
    val_b = False
    result = check_both_false(val_a, val_b)
    print(result)
    val_c = True
    val_d = False
    result2 = check_both_false(val_c, val_d)
    print(result2)