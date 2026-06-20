def check_condition(x, y):
    return x and y
if __name__ == '__main__':
    print(check_condition(True, True))
    print(check_condition(False, True))
    print(check_condition(True, False))
    print(check_condition(False, False))