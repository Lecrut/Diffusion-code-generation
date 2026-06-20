def is_odd(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n & 1 == 1

if __name__ == '__main__':
    try:
        print(is_odd(3))
        print(is_odd(4))
        print(is_odd('a'))
    except ValueError as e:
        print(e)