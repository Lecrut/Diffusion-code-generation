is_zero = lambda x: x == 0 or (abs(x) < 1e-09 and isinstance(x, float))
if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(-0.0))
    print(is_zero(123))
    print(is_zero(0.001))
    print(is_zero(1e-10))
    print(is_zero(1))