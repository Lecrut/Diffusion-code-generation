def is_zero(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a numeric value")
    return abs(number) < 1e-9

if __name__ == '__main__':
    print(f"is_zero(0): {is_zero(0)}")
    print(f"is_zero(5): {is_zero(5)}")
    print(f"is_zero(-0): {is_zero(-0)}")
    print(f"is_zero(3.14): {is_zero(3.14)}")
    print(f"is_zero('0'): {is_zero('0')}")