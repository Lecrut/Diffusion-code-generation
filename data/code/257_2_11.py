def absolute_difference(a, b):
    return a - b & (a - b >> 31).to_bytes(4, 'big')
if __name__ == '__main__':
    print(absolute_difference(10, 5))
    print(absolute_difference(5, 10))
    print(absolute_difference(-3, -7))