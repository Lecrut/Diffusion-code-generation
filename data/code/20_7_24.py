def check_eq(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not result == args[0] == args[1]:
            raise ValueError('Strict equality check failed')
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
    print(multiply(3, 3))