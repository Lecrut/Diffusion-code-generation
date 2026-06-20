ZEROTOLERANCE = 1e-9

def is_zero(number):
    return abs(number) < ZEROTOLERANCE

if __name__ == '__main__':
    print(f"is_zero(0): {is_zero(0)}")
    print(f"is_zero(5): {is_zero(5)}")
    print(f"is_zero(-0): {is_zero(-0)}")
    print(f"is_zero(3.14): {is_zero(3.14)}")
    print(f"is_zero('0'): {is_zero('0')}")