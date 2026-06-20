ZERO_THRESHOLD = 1e-9

def is_zero(number):
    return abs(number) < ZERO_THRESHOLD

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(1e-10))
    print(is_zero(1e-8))