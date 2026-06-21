def is_strictly_greater(func):
    def wrapper(a, b):
        if not (a > b):
            raise ValueError(f'The first argument {a} must be strictly greater than the second argument {b}.')
        return func(a, b)
    return wrapper

@is_strictly_greater
def multiply(a, b):
    return a * b

if __name__ == '__main__':
    try:
        result = multiply(7, 3)
        print(result)
    except ValueError as e:
        print(e)