IS_ODD = lambda n: (n & 1) == 1

if __name__ == '__main__':
    print(IS_ODD(5))
    print(IS_ODD(4))
    print(IS_ODD(0))
    print(IS_ODD(-3))