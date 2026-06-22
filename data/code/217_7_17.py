def is_greater(a, b):
    return a > b if a >= 0 else b < 0
if __name__ == '__main__':
    print(is_greater(5, 3))
    print(is_greater(-1, -2))
    print(is_greater(0, 0))