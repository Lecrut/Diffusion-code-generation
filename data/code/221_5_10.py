def validate_numbers(a, b, c):
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        raise ValueError("All inputs must be integers.")
    if len({a, b, c}) != 3:
        raise ValueError("The numbers must be distinct.")

def sort_three_numbers(a, b, c):
    validate_numbers(a, b, c)
    if a <= b <= c:
        return a, b, c
    elif a <= c <= b:
        return a, c, b
    elif b <= a <= c:
        return b, a, c
    elif b <= c <= a:
        return b, c, a
    elif c <= a <= b:
        return c, a, b
    else:
        return c, b, a

if __name__ == '__main__':
    print(sort_three_numbers(5, 2, 8))
    print(sort_three_numbers(100, 42, 34))