def check_complex_condition(a, b, c):
    if a > 0:
        if b < 0:
            return True
        elif c == 0:
            return False
    elif b >= 0:
        return False
    elif c != 0:
        return True
if __name__ == '__main__':
    print(check_complex_condition(1, -2, 0))
    print(check_complex_condition(-3, 4, 5))