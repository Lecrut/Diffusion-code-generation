def is_odd(n: int) -> bool:
    return n & 1 == 1

if __name__ == '__main__':
    print(is_odd(3))  # True
    print(is_odd(4))  # False