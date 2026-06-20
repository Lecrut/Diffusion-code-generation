def validate_numbers(*args):
    if not all((isinstance(arg, int) for arg in args)):
        raise ValueError('All arguments must be integers')
    return True

def sum_three(a, b, c):
    if validate_numbers(a, b, c):
        return a + b + c
if __name__ == '__main__':
    result = sum_three(1, 2, 3)
    print(result)