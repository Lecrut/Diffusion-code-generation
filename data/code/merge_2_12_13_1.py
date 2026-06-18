def is_odd(n: int) -> bool:
    return n % 2 != 0
if __name__ == '__main__':
    print(is_odd(7))
    print(is_odd(10))
    print(is_odd(-3))
    print(is_odd(0))