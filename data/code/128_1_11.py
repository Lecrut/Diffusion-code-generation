def is_negative(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be an integer or float")
    return number < 0

if __name__ == '__main__':
    print(is_negative(-5))
    print(is_negative(0))
    print(is_negative(10.5))
    print(is_negative(-0.001))