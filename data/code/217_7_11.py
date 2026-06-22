def is_greater(a, b):
    return a - b >> 31 & 1
if __name__ == '__main__':
    print(is_greater(5, 3))
    print(is_greater(3, 5))