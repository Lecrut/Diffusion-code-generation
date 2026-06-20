def check_zero(value):
    return value == 0

if __name__ == '__main__':
    print(check_zero(0))
    print(check_zero(42))
    print(check_zero(-1))
    print(check_zero(0.0))
    print(check_zero("0"))