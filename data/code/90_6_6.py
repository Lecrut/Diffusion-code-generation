def check_conditions(a, b, c):
    return a | b | c != 0
if __name__ == '__main__':
    print(check_conditions(1, 2, 4))
    print(check_conditions(0, 0, 0))