def check_eq(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not result:
            raise ValueError('Function did not return True')
        return result
    return wrapper

@check_eq
def add(a, b):
    return a == b
if __name__ == '__main__':
    print(add(5, 5))
    try:
        print(add(5, 10))
    except ValueError as e:
        print(e)