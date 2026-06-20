def custom_and(a, b):
    return a * b

def custom_or(a, b):
    return a + b - a * b

def custom_not(a):
    if not isinstance(a, int) or a not in (0, 1):
        raise ValueError('Input must be 0 or 1')
    return 1 - a
if __name__ == '__main__':
    print(custom_and(1, 1))
    print(custom_and(0, 1))
    print(custom_or(1, 0))
    print(custom_or(0, 0))
    try:
        print(custom_not(2))
    except ValueError as e:
        print(e)