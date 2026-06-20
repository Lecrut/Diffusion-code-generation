def length_difference(a, b):
    return a - b if a > b else b - a

if __name__ == '__main__':
    val1 = 10
    val2 = 4
    print(length_difference(val1, val2))
    val3 = 3
    val4 = 7
    print(length_difference(val3, val4))