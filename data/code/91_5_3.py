def negate_decorator(flag):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, bool):
                return not result
            return result
        return inner
    return wrapper

@negate_decorator(True)
def check_status():
    return True

if __name__ == '__main__':
    result = check_status()
    print(result)