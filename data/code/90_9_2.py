def check_condition(*args):
    result = False
    for arg in args:
        if arg:
            result = True
            break
    return result

if __name__ == '__main__':
    print(check_condition(True, False, False))
    print(check_condition(False, False, True))
    print(check_condition(False, False, False))