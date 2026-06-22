def absolute_difference(a, b):
    return a - b & 4294967295 if a - b < 0 else a - b
if __name__ == '__main__':
    print(absolute_difference(10, 5))
    print(absolute_difference(3, 9))