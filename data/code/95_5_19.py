def validate_integers(a, b, c):
    if not all(isinstance(x, int) for x in [a, b, c]):
        raise ValueError("All inputs must be integers")

def check_conditions(a, b, c):
    pos_a = a > 0
    even_b = b % 2 == 0
    divisible_c_by_a = c % a == 0
    return (pos_a, even_b, divisible_c_by_a)

if __name__ == '__main__':
    try:
        validate_integers(15, 22, 60)
        result = check_conditions(15, 22, 60)
        print(result)
    except ValueError as e:
        print(e)