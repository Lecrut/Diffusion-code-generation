def is_zero(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or float")
    return value == 0

if __name__ == '__main__':
    print(f"is_zero(0): {is_zero(0)}")
    print(f"is_zero(5): {is_zero(5)}")
    try:
        print(f"is_zero('0'): {is_zero('0')}")
    except ValueError as e:
        print(e)