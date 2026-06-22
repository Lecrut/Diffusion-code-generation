def negate_decorator(flag):
    def wrapper(func):
        def inner(*args, **kwargs):
            return not flag
        return inner
    return wrapper

@negate_decorator(True)
def check_value():
    return True

if __name__ == '__main__':
    result = check_value()
    print(result)