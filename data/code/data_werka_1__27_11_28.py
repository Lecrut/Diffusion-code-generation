def check_difference(a, b):
    return a != b

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    is_different = check_difference(value1, value2)
    print(is_different)