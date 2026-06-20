def check_truthiness(value1, value2):
    return bool(value1) and bool(value2)
if __name__ == '__main__':
    print(check_truthiness(True, True))
    print(check_truthiness(True, False))
    print(check_truthiness(False, True))
    print(check_truthiness(False, False))