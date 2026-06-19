def check_eq(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not all((isinstance(arg, type(result)) for arg in args)):
            raise TypeError('All arguments must be of the same type as the return value')
        return result
    return wrapper

@check_eq
def add(a, b):
    return a + b

@check_eq
def multiply(a, b):
    return a * b
if __name__ == '__main__':
    print(add(2, 3))
    print(multiply(4, 5))