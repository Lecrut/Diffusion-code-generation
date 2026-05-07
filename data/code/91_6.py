def negate_if(should_negate):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return not func(*args, **kwargs)
        return wrapper
    return decorator
@negate_if(True)
def my_function(x):
    return x
if __name__ == '__main__':
    result = my_function(5)
    print(result)