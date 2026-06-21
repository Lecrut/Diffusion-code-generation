def negate_boolean(negate: bool):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if negate:
                return not result
            return result
        return wrapper
    return decorator

@negate_boolean(True)
def check_value(x):
    return x > 0

if __name__ == '__main__':
    result = check_value(5)
    print(result)
    result_false = check_value(-1)
    print(result_false)