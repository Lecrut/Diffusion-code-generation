def negate_decorator(flag):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if flag:
                return not result
            return result
        return inner
    return wrapper

@negate_decorator(True)
def check_value(x):
    return x

if __name__ == '__main__':
    result = check_value(True)
    print(result)