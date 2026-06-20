def check_condition(num):
    return num > 0 and num & 1 == 0
if __name__ == '__main__':
    print(check_condition(4))
    print(check_condition(-2))
    print(check_condition(3))
    print(check_condition(0))