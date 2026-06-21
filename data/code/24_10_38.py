is_negative = lambda x: False if x >= 0 else True

if __name__ == '__main__':
    print(is_negative(-1))
    print(is_negative(0))
    print(is_negative(1))
    print(is_negative(-10))
    print(is_negative(25))