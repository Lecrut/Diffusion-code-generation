is_zero = lambda x: abs(x) < 1e-09
if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero(1e-10))
    print(is_zero(1e-08))
    print(is_zero(-1e-09))
    print(is_zero(1))