def length_difference(a, b):
    return a - b if a >= b else b - a

if __name__ == '__main__':
    print(length_difference(5, 3))
    print(length_difference(3, 5))
    print(length_difference(10, 10))