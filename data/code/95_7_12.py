def validate_inputs(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError("All arguments must be integers.")
    if a <= 0:
        raise ValueError("The first argument must be positive.")
    if b % 2 != 0:
        raise ValueError("The second argument must be even.")

def check_conditions(a, b, c):
    validate_inputs(a, b, c)
    return (c % (a * b)) == 0

if __name__ == '__main__':
    print(check_conditions(2, 4, 8))
    print(check_conditions(3, 6, 9))
    print(check_conditions(-1, 2, 4))
    print(check_conditions(2, 3, 5))
    print(check_conditions(5, 4, 20))
    print(check_conditions(1, 2, 5))
    print(check_conditions(1, 3, 5))