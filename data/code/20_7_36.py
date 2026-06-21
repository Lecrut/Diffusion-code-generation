def check_eq(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, tuple) or len(result) != 2:
            raise ValueError('Function must return a tuple of two elements')
        a, b = result
        if a == b:
            return True
        else:
            return False
    return wrapper

@check_eq
def sample_function(x, y):
    return (x, y)
if __name__ == '__main__':
    print(sample_function(10, 10))
    print(sample_function(10, 20))