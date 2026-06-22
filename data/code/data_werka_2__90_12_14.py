def check_or_condition(a: bool, b: bool) -> bool:
    mask = 0x1
    val_a = 1 if a else 0
    val_b = 1 if b else 0
    return bool((val_a | val_b) & mask)

if __name__ == '__main__':
    result = check_or_condition(True, False)
    print(result)
    result2 = check_or_condition(False, False)
    print(result2)