def is_positive(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number.")
    return value > 0
if __name__ == '__main__':
    print(is_positive(5))
    print(is_positive(-3.5))
    print(is_positive(0))
    try:
        is_positive("not a number")
    except TypeError as e:
        print(e)