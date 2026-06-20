def check_conditions(a, b, c):
    return a | b | c != 0
if __name__ == '__main__':
    print(check_conditions(0, 0, 0))
    print(check_conditions(1, 0, 0))
    print(check_conditions(0, 1, 0))
    print(check_conditions(0, 0, 1))
    print(check_conditions(1, 1, 0))
    print(check_conditions(0, 1, 1))
    print(check_conditions(1, 0, 1))
    print(check_conditions(1, 1, 1))