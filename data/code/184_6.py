import functools
def check_docstring_keyword(keyword):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            docstring = func.__doc__
            if docstring is None or keyword not in docstring:
                raise TypeError(f"Missing required keyword '{keyword}' in the docstring of function '{func.__name__}'.")
            return func(*args, **kwargs)
        return wrapper
    return decorator
@check_docstring_keyword("Args")
def sample_function_with_args(a, b):
    return a + b
@check_docstring_keyword("Returns")
def sample_function_with_returns(x, y):
    return x + y
def sample_function_missing():
    pass
if __name__ == '__main__':
    try:
        result1 = sample_function_with_args(5, 3)
        print(f"Result 1: {result1}")
        result2 = sample_function_with_returns(10, 5)
        print(f"Result 2: {result2}")
        sample_function_missing()
    except TypeError as e:
        print(f"Caught expected error: {e}")