def conditional_execution(condition_a, condition_b):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition_a and condition_b:
                return func(*args, **kwargs)
            else:
                return None
        return wrapper
    return decorator
@conditional_execution(True, False)
def my_function(x, y):
    return x + y
@conditional_execution(False, True)
def another_function(x, y):
    return x * y
if __name__ == '__main__':
    print(my_function(5, 3))
    print(another_function(5, 3))