def is_odd(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    return n & 1

if __name__ == '__main__':
    print(is_odd(4))
    print(is_odd(5))