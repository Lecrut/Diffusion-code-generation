def check_difference(a, b):
    return a != b
if __name__ == '__main__':
    val1 = 5
    val2 = 10
    print(check_difference(val1, val2))
    val3 = 7
    val4 = 7
    print(check_difference(val3, val4))
    val5 = -1
    val6 = 1
    print(check_difference(val5, val6))