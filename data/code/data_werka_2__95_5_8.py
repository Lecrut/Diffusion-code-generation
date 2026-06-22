def validate_and_check(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError("All inputs must be integers")
    
    if a == 0:
        raise ValueError("First integer must not be zero for divisibility check")
        
    is_positive = a > 0
    is_even = b % 2 == 0
    is_divisible = c % a == 0
    
    return (is_positive, is_even, is_divisible)

if __name__ == '__main__':
    val_a = 3
    val_b = 7
    val_c = 9
    outcome = validate_and_check(val_a, val_b, val_c)
    print(outcome)