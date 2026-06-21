def negate_decorator(flag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if flag:
                return not func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@negate_decorator(True)
def is_true(value):
    return value

if __name__ == '__main__':
    result = is_true(True)
    print(result)