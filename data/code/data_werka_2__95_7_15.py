def validate_triple(first, second, third):
    POSITIVE_THRESHOLD = 0
    EVEN_MODULUS = 2
    if first <= POSITIVE_THRESHOLD:
        return False
    if second % EVEN_MODULUS != 0:
        return False
    combined_factor = first * second
    if combined_factor == 0:
        return False
    return third % combined_factor == 0

if __name__ == '__main__':
    val_a = 3
    val_b = 6
    val_c = 18
    outcome = validate_triple(val_a, val_b, val_c)
    print(outcome)