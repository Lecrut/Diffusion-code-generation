def custom_and(a, b):
    if not a:
        return 0
    return b

def custom_or(a, b):
    if a:
        return 1
    return b

def custom_not(a):
    return 1 - a
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