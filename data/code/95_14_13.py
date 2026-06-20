def check_conditions(a, b, c):
    if a > 0 and b < a and c == a + b:
        return True
    return False

if __name__ == '__main__':
    print(check_conditions(5.0, 2.5, 7.5))