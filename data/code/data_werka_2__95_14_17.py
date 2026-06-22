def check_conditions(a: float, b: float, c: float) -> bool:
    if a <= 0:
        return False
    if b >= a:
        return False
    if c != a + b:
        return False
    return True

if __name__ == '__main__':
    val_a = 10.0
    val_b = 3.0
    val_c = 13.0
    print(check_conditions(val_a, val_b, val_c))