def check_conditions(a, b, c):
    POSITIVE = 0
    if a > POSITIVE and b < a and c == (a + b):
        return True
    return False

if __name__ == '__main__':
    result = check_conditions(5.0, 3.0, 8.0)
    print(result)