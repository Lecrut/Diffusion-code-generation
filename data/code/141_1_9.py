def custom_and(a, b):
    return int(a and b)

def custom_or(a, b):
    return int(a or b)

def custom_not(a):
    return int(not a)
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