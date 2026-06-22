def is_strictly_greater(func):

    def wrapper(a, b):
        if a > b:
            return func(a, b)
        else:
            raise ValueError('First argument must be strictly greater than the second argument.')
    return wrapper

@is_strictly_greater
def add(a, b):
    return a + b
if __name__ == '__main__':
    try:
        result = add(10, 5)
        print(result)
    except ValueError as e:
        print(e)
    try:
        result = add(5, 10)
        print(result)
    except ValueError as e:
        print(e)