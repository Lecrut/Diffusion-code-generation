def validate_and_check(a: int, b: int, c: int) -> tuple:
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError("All inputs must be integers")
    if a == 0:
        raise ValueError("First argument cannot be zero for divisibility check")
    
    check_positive = a > 0
    check_even = b % 2 == 0
    check_divisible = c % a == 0
    
    return (check_positive, check_even, check_divisible)

if __name__ == '__main__':
    sample_a = 3
    sample_b = 8
    sample_c = 15
    
    output = validate_and_check(sample_a, sample_b, sample_c)
    print(output)