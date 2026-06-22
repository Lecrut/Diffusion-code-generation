def is_strictly_greater(func):

    def wrapper(a, b):
        if a <= b:
            raise ValueError('First argument must be strictly greater than the second argument.')
        return func(a, b)
    return wrapper

@is_strictly_greater
def subtract(a, b):
    return a - b
if __name__ == '__main__':
    try:
        result = subtract(10, 5)
        print(result)
    except ValueError as e:
        print(e)
    try:
        result = subtract(3, 4)
        print(result)
    except ValueError as e:
        print(e)