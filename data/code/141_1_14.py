def custom_and(a, b):
    return a == 1 and b == 1

def custom_or(a, b):
    return a == 1 or b == 1

def custom_not(a):
    return not a == 1
if __name__ == '__main__':
    print(custom_and(1, 0))
    print(custom_or(0, 1))
    print(custom_not(1))