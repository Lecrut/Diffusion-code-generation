def _validate_positive_integers(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError("All inputs must be integers")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All inputs must be positive")
    return True

def evaluate_triple(a, b, c):
    _validate_positive_integers(a, b, c)
    sum_val = a + b + c
    if sum_val > 100 and a > b:
        result = "High sum with a dominant"
    elif sum_val <= 50 and c == b:
        result = "Low sum with equal b and c"
    elif a == b == c:
        result = "All values identical"
    else:
        result = "Mixed conditions"
    return result

if __name__ == '__main__':
    val_a = 30
    val_b = 20
    val_c = 60
    output = evaluate_triple(val_a, val_b, val_c)
    print(output)
    val_a = 10
    val_b = 10
    val_c = 10
    output = evaluate_triple(val_a, val_b, val_c)
    print(output)