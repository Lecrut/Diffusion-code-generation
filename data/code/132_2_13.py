def is_positive(n):
    return n > 0

def is_even(n):
    return not (n & 1)

def check_condition(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    return is_positive(n) and is_even(n)

if __name__ == '__main__':
    print(check_condition(4))
    print(check_condition(-2))
    print(check_condition(0))
    print(check_condition(3))