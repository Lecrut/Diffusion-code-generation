ZERO = 0

def is_zero(value):
    return value == ZERO

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(42))
    print(is_zero(-1))
    print(is_zero(3.14))
    print(is_zero(ZERO))