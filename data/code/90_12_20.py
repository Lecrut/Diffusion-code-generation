def check_or_condition(a: bool, b: bool) -> bool:
    bits = {
        False: 0,
        True: 1,
    }
    val_a = bits[a]
    val_b = bits[b]
    return bool(val_a | val_b)

if __name__ == '__main__':
    result = check_or_condition(True, False)
    print(result)