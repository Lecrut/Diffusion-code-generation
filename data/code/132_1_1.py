def check_and_combine(a, b):
    return a or b
if __name__ == '__main__':
    print(check_and_combine(True, False))
    print(check_and_combine(False, True))
    print(check_and_combine(True, True))
    print(check_and_combine(False, False))