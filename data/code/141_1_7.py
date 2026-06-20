def validate_input(value):
    if value not in [0, 1]:
        raise ValueError('Input must be either 0 or 1')

def custom_and(a, b):
    validate_input(a)
    validate_input(b)
    return a * b

def custom_or(a, b):
    validate_input(a)
    validate_input(b)
    return a + b - a * b

def custom_not(a):
    validate_input(a)
    return 1 - a
if __name__ == '__main__':
    print(custom_and(1, 1))
    print(custom_or(0, 1))
    print(custom_not(0))