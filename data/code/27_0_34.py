def check_difference(num1, num2):
    return num1 != num2

if __name__ == '__main__':
    print(check_difference(5, 3))
    print(check_difference(7.0, 7))
    print(check_difference('a', 'b'))
    print(check_difference(True, False))