check_odd = lambda n: isinstance(n, int) and n % 2 != 0
if __name__ == '__main__':
    print(check_odd(3))
    print(check_odd(4))
    print(check_odd(-3))
    print(check_odd(0))