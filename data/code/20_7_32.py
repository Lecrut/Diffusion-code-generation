def check_eq(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, tuple) or len(result) != 2:
            raise ValueError('Function must return a tuple of two values to compare.')
        a, b = result
        if a == b:
            return True
        else:
            return False
    return wrapper

@check_eq
def add_and_check(x, y):
    return (x + y, 5)
if __name__ == '__main__':
    print(add_and_check(2, 3))
    print(add_and_check(1, 4))