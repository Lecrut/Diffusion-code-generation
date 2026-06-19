def check_eq(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not all((result == arg for arg in args[1:])):
            raise ValueError('All results must be strictly equal')
        return result
    return wrapper

@check_eq
def add(a, b):
    return a + b

@check_eq
def multiply(a, b):
    return a * b
if __name__ == '__main__':
    print(add(2, 2))
    try:
        print(add(2, 3))
    except ValueError as e:
        print(e)
    print(multiply(3, 3))
    try:
        print(multiply(3, 4))
    except ValueError as e:
        print(e)