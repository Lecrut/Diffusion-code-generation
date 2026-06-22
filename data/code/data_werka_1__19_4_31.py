def check_truth(condition):

    def decorator(func):

        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                return None
        return wrapper
    return decorator

@check_truth(True)
def example_function(x, y):
    return x + y

@check_truth(False)
def disabled_function(x, y):
    return x * y
if __name__ == '__main__':
    result1 = example_function(3, 4)
    print(result1)
    result2 = disabled_function(3, 4)
    print(result2)