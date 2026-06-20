def is_odd(n: int) -> bool:
    return n & 1

if __name__ == '__main__':
    print(is_odd(7))  # True
    print(is_odd(10))  # False
    print(is_odd(0))  # False
    print(is_odd(-3))  # True