def length_difference(a, b):
    return a - b if a >= b else b - a

if __name__ == '__main__':
    print(length_difference(10, 3))
    print(length_difference(5, 8))
    print(length_difference(7, 7))