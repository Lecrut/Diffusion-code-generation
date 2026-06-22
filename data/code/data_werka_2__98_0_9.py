def _validate_positive_integers(a, b, c):
    if not isinstance(a, int) or a <= 0:
        raise ValueError("a must be a positive integer")
    if not isinstance(b, int) or b <= 0:
        raise ValueError("b must be a positive integer")
    if not isinstance(c, int) or c <= 0:
        raise ValueError("c must be a positive integer")
    return True

def evaluate_boolean_logic(a, b, c):
    _validate_positive_integers(a, b, c)
    
    if a > 50 and b < 10:
        category = "High A, Low B"
    elif c == 100:
        category = "C is Hundred"
    elif a + b > c:
        category = "Sum Greater"
    elif a == b == c:
        category = "All Equal"
    else:
        category = "Default Case"
    
    return {
        "category": category,
        "sum": a + b + c,
        "product": a * b * c
    }

if __name__ == '__main__':
    val_a = 60
    val_b = 5
    val_c = 20
    
    result = evaluate_boolean_logic(val_a, val_b, val_c)
    print(result)