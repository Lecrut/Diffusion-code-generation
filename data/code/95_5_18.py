def validate_positive(value):
    return value > 0

def validate_even(value):
    return value % 2 == 0

def validate_divisible(numerator, denominator):
    if denominator == 0:
        raise ValueError("Divisor cannot be zero")
    return numerator % denominator == 0

def check_integers(a, b, c):
    pos_check = validate_positive(a)
    even_check = validate_even(b)
    div_check = validate_divisible(c, a)
    return (pos_check, even_check, div_check)

if __name__ == '__main__':
    sample_a = 7
    sample_b = 8
    sample_c = 21
    result = check_integers(sample_a, sample_b, sample_c)
    print(result)