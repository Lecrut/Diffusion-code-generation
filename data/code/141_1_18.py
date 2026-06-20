def custom_and(a, b):
    return int(a * b)

def custom_or(a, b):
    return int(a + b - a * b)

def custom_not(a):
    return 1 - int(a)

if __name__ == '__main__':
    a_val = 0
    b_val = 1
    print(custom_and(a_val, b_val))
    print(custom_or(a_val, b_val))
    print(custom_not(a_val))

    a_val = 1
    b_val = 0
    print(custom_and(a_val, b_val))
    print(custom_or(a_val, b_val))
    print(custom_not(b_val))

    a_val = 1
    b_val = 1
    print(custom_and(a_val, b_val))
    print(custom_or(a_val, b_val))
    print(custom_not(a_val))