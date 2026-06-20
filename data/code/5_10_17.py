def length_difference(a, b):
    return a - b if a > b else b - a

if __name__ == '__main__':
    print(length_difference(10, 5))
    print(length_difference(3, 8))
    print(length_difference(7, 7))
    print(length_difference(0, 12))
    print(length_difference(12, 0))