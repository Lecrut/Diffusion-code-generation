def is_odd(n: int) -> bool:
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n & 1 == 1

if __name__ == '__main__':
    print(is_odd(3))  # True
    print(is_odd(4))  # False