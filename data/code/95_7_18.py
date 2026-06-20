def validate_input(a, b, c):
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        raise ValueError("All arguments must be integers")
    if a <= 0:
        raise ValueError("First argument must be positive")
    if b % 2 != 0:
        raise ValueError("Second argument must be even")

def combine_conditions(a, b, c):
    validate_input(a, b, c)
    return (c % (a * b)) == 0

if __name__ == '__main__':
    print(combine_conditions(2, 4, 6))
    print(combine_conditions(3, 5, 7))
    print(combine_conditions(-1, 2, 4))
    print(combine_conditions(2, 3, 5))
    print(combine_conditions(5, 4, 10))
    print(combine_conditions(1, 2, 5))
    print(combine_conditions(1, 3, 5))