check_odd = lambda n: (n & 1) == 1

if __name__ == '__main__':
    print(check_odd(5))
    print(check_odd(4))
    print(check_odd(0))
    print(check_odd(-3))