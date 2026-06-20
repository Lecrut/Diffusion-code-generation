def custom_and(a, b):
    return a * b

def custom_or(a, b):
    return max(a, b)

def custom_not(a):
    return 1 - a
if __name__ == '__main__':
    print(custom_and(0, 1))
    print(custom_or(0, 1))
    print(custom_not(0))