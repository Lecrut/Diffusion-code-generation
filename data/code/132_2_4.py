def check_condition(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n > 0 and (not n & 1)

if __name__ == '__main__':
    try:
        print(check_condition(4))
        print(check_condition(-2))
        print(check_condition(0))
        print(check_condition(3))
        print(check_condition('a'))
    except ValueError as e:
        print(e)