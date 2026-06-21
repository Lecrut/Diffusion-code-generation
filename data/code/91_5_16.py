def negate_decorator(flag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, bool):
                return not result
            return result
        return wrapper
    return decorator

@negate_decorator(True)
def check_status():
    return True

if __name__ == '__main__':
    result = check_status()
    print(result)