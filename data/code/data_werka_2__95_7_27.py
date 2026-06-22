def verify_conditions(first, second, third):
    IS_POSITIVE_THRESHOLD = 0
    IS_EVEN_MODULUS = 2
    if first <= IS_POSITIVE_THRESHOLD:
        return False
    if second % IS_EVEN_MODULUS != 0:
        return False
    combined_factor = first * second
    if combined_factor == 0:
        return False
    return third % combined_factor == 0

if __name__ == '__main__':
    val1 = 3
    val2 = 6
    val3 = 18
    outcome = verify_conditions(val1, val2, val3)
    print(outcome)