def is_strictly_greater(func):

    def wrapper(a, b):
        if a <= b:
            raise ValueError(f'The first argument {a} must be strictly greater than the second argument {b}.')
        return func(a, b)
    return wrapper

@is_strictly_greater
def add_numbers(x, y):
    return x + y
if __name__ == '__main__':
    try:
        result = add_numbers(10, 5)
        print(result)
    except ValueError as e:
        print(e)
    try:
        result = add_numbers(3, 7)
        print(result)
    except ValueError as e:
        print(e)