def length_diff(a, b):
    return a - b if a > b else b - a

if __name__ == '__main__':
    print(length_diff(10, 3))
    print(length_diff(3, 10))
    print(length_diff(5, 5))