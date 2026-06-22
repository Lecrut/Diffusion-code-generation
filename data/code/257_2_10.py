def absolute_difference(a, b):
    return a - b & 4294967295
if __name__ == '__main__':
    print(absolute_difference(5, 3))
    print(absolute_difference(-1, -4))
    print(absolute_difference(0, 0))