ZERO_THRESHOLD = 1e-9

def is_zero(num):
    return abs(num) < ZERO_THRESHOLD

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(42))
    print(is_zero(-1.5))
    print(is_zero(1e-09))
    print(is_zero(1e-10))