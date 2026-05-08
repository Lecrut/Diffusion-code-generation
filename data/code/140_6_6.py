def conditional_execution(condition1, condition2=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition1:
                if condition2 is None or condition2:
                    return func(*args, **kwargs)
                else:
                    return None
            else:
                return None
        return wrapper
    return decorator
@conditional_execution(True, False)
def my_function(a, b):
    return a + b
@conditional_execution(False)
def another_function(x, y):
    return x * y
if __name__ == '__main__':
    print(my_function(5, 10))
    print(another_function(2, 3))