FIRST_CONSTANT = 5
SECOND_CONSTANT = 3

def validate_constants(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('Both constants must be integers.')

def add_constants(x, y):
    validate_constants(x, y)
    return x + y
if __name__ == '__main__':
    result = add_constants(FIRST_CONSTANT, SECOND_CONSTANT)
    print(result)