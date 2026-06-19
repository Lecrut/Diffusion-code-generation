def is_zero(number):
    return number == 0
if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(1))
    print(is_zero(-1))
    print(is_zero(0.0))
    print(is_zero(1e-10))