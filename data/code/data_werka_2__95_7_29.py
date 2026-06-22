def validate_combination(first, second, third):
    if first <= 0:
        return False
    if second % 2 != 0:
        return False
    divisor = first * second
    if divisor == 0:
        return False
    return third % divisor == 0

if __name__ == '__main__':
    val_a = 3
    val_b = 6
    val_c = 18
    output = validate_combination(val_a, val_b, val_c)
    print(output)