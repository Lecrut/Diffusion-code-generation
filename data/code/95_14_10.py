def check_conditions(a, b, c):
    if a <= 0:
        return False
    if b >= a:
        return False
    if c != a + b:
        return False
    return True

if __name__ == '__main__':
    result = check_conditions(5.0, -3.0, 2.0)
    print(result)