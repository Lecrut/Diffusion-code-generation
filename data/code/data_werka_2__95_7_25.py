def validate_parameters(a, b, c):
    if not (a > 0 and b % 2 == 0 and c % (a * b) == 0):
        return False
    return True
if __name__ == '__main__':
    val_a = 3
    val_b = 4
    val_c = 12
    outcome = validate_parameters(val_a, val_b, val_c)
    print(outcome)