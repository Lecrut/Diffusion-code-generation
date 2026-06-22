def check_conditions(a: float, b: float, c: float) -> bool:
    if a <= 0:
        return False
    if b >= a:
        return False
    return c == a + b

if __name__ == '__main__':
    val_a = 3.14
    val_b = 1.2
    val_c = 4.34
    output = check_conditions(val_a, val_b, val_c)
    print(output)