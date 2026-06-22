def combine_checks(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError("Inputs must be integers")
    if a == 0:
        raise ValueError("First input cannot be zero")
    if a <= 0:
        raise ValueError("First input must be positive")
    if b % 2 != 0:
        raise ValueError("Second input must be even")
    if c % a != 0:
        raise ValueError("Third input must be divisible by the first")
    return True

if __name__ == '__main__':
    try:
        result1 = combine_checks(2, 4, 8)
        print(result1)
    except ValueError as e:
        print(e)
    try:
        result2 = combine_checks(3, 4, 12)
        print(result2)
    except ValueError as e:
        print(e)
    try:
        result3 = combine_checks(-1, 4, 8)
        print(result3)
    except ValueError as e:
        print(e)
    try:
        result4 = combine_checks(1, 5, 10)
        print(result4)
    except ValueError as e:
        print(e)
    try:
        result5 = combine_checks(5, 6, 10)
        print(result5)
    except ValueError as e:
        print(e)