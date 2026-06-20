def is_negative(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be an integer or float")
    return num < 0

if __name__ == '__main__':
    x = -5
    print(is_negative(x))