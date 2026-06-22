def absolute_length_difference(a, b):
    return a - b if a > b else b - a

if __name__ == '__main__':
    print(absolute_length_difference(10, 7))
    print(absolute_length_difference(3, 9))
    print(absolute_length_difference(5, 5))