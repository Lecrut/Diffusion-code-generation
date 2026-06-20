ZERO = 0

def is_zero(number):
    return number == ZERO

if __name__ == '__main__':
    print(f"is_zero(0): {is_zero(ZERO)}")
    print(f"is_zero(5): {is_zero(5)}")
    print(f"is_zero(-0): {is_zero(-ZERO)}")
    print(f"is_zero(3.14): {is_zero(3.14)}")
    print(f"is_zero('0'): {is_zero(ZERO)}")