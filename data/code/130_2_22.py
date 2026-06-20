ZERO_THRESHOLD = 1e-9

def is_zero(value):
    if isinstance(value, float):
        return abs(value) < ZERO_THRESHOLD
    return value == 0

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero(-0))
    print(is_zero(-0.0))
    print(is_zero(1))
    print(is_zero(1.0))