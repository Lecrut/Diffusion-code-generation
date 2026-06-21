ZERO_THRESHOLD = 1e-09

is_zero = lambda x: abs(x) < ZERO_THRESHOLD

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(-0.0))
    print(is_zero(123456789))
    print(is_zero(ZERO_THRESHOLD / 2))
    print(is_zero(ZERO_THRESHOLD * 2))
    print(is_zero(1))