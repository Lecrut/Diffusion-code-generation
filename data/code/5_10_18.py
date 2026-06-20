def absolute_difference(len_a, len_b):
    return len_a - len_b if len_a > len_b else len_b - len_a

if __name__ == '__main__':
    print(absolute_difference(10, 5))
    print(absolute_difference(5, 10))
    print(absolute_difference(3, 3))