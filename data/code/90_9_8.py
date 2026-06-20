def check_condition(*args):
    for arg in args:
        if arg:
            return True
    return False

if __name__ == '__main__':
    print(check_condition(True, False, False))
    print(check_condition(False, False, True))
    print(check_condition(False, False, False))