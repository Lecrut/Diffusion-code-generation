def custom_and(a, b):
    return a and b

def custom_or(a, b):
    return a or b

def custom_not(a):
    return not a
if __name__ == '__main__':
    print(custom_and(True, True))
    print(custom_and(False, True))
    print(custom_and(True, False))
    print(custom_and(False, False))
    print(custom_or(True, True))
    print(custom_or(False, True))
    print(custom_or(True, False))
    print(custom_or(False, False))
    print(custom_not(True))
    print(custom_not(False))