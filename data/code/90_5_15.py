def or_condition_test(condition):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not any((cond(result) for cond in condition)):
                raise ValueError(f"Function {func.__name__} did not meet the 'or' condition.")
            return result
        return wrapper
    return decorator

@or_condition_test([lambda x: x > 0, lambda x: isinstance(x, str)])
def test_function(x):
    return x
if __name__ == '__main__':
    try:
        print(test_function(5))
        print(test_function('hello'))
        print(test_function(-1))
    except ValueError as e:
        print(e)