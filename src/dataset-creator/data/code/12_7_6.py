def is_odd(n):
    return n % 2 != 0 if isinstance(n, int) else False
if __name__ == '__main__':
    print(is_odd(5))
    print(is_odd(-3))
    print(is_odd(10))