def check_eq(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, tuple) or len(result) != 2:
            raise ValueError('Function must return a tuple of two values to compare.')
        if result[0] != result[1]:
            raise AssertionError(f'Values {result[0]} and {result[1]} are not strictly equal.')
        return result
    return wrapper

@check_eq
def sample_function(x, y):
    return (x, y)
if __name__ == '__main__':
    try:
        print(sample_function(5, 5))
        print(sample_function('hello', 'hello'))
        print(sample_function(3, 4))
    except Exception as e:
        print(e)