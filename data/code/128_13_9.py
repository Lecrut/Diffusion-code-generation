def is_negative(num):
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a number")
    return num < 0

if __name__ == '__main__':
    print(is_negative(-5))
    print(is_negative(3))
    print(is_negative(0))
    print(is_negative(-1.5))