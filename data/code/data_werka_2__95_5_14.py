def validate_positive(value):
    return value > 0

def validate_even(value):
    return value % 2 == 0

def validate_divisible(dividend, divisor):
    if divisor == 0:
        return False
    return dividend % divisor == 0

def check_integers(a, b, c):
    pos_check = validate_positive(a)
    even_check = validate_even(b)
    div_check = validate_divisible(c, a)
    return (pos_check, even_check, div_check)

if __name__ == '__main__':
    result = check_integers(7, 8, 21)
    print(result)