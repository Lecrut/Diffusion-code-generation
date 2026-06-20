def is_zero(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Only numeric types (int, float) are supported.")
    return value == 0

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(-1))
    print(is_zero(1))
    print(is_zero(0.0))
    print(is_zero(-0.0))
    try:
        is_zero("a")
    except TypeError as e:
        print(f"Error caught: {e}")