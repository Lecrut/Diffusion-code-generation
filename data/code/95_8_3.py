def check_condition(a, b, c):
    if a > 0 and b % 2 == 0 and c % (a * b) == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    print(check_condition(3, 4, 12))
    print(check_condition(2, 6, 12))
    print(check_condition(1, 2, 4))
    print(check_condition(5, 4, 20))
    print(check_condition(10, 2, 10))