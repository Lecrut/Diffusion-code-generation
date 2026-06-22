def is_greater(a, b):
    diff = a - b
    return diff >> 31 & 1
if __name__ == '__main__':
    print(is_greater(5, 3))
    print(is_greater(2, 4))