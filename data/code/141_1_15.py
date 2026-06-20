def custom_and(a, b):
    return int(bool(a) and bool(b))

def custom_or(a, b):
    return int(bool(a) or bool(b))

def custom_not(a):
    return int(not bool(a))
if __name__ == '__main__':
    print(custom_and(1, 1))
    print(custom_and(0, 1))
    print(custom_and(1, 0))
    print(custom_and(0, 0))
    print(custom_or(1, 1))
    print(custom_or(0, 1))
    print(custom_or(1, 0))
    print(custom_or(0, 0))
    print(custom_not(1))
    print(custom_not(0))