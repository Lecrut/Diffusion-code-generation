def is_zero(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")
    return value == 0

if __name__ == '__main__':
    print(f"is_zero(0): {is_zero(0)}")
    print(f"is_zero(5): {is_zero(5)}")
    print(f"is_zero(-0): {is_zero(-0)}")
    print(f"is_zero(3.14): {is_zero(3.14)}")
    print(f"is_zero('0'): {is_zero('0')}")