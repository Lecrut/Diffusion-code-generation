def negate_decorator(flag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not isinstance(flag, bool):
                raise ValueError("flag must be a boolean")
            return not flag
        return wrapper
    return decorator

@negate_decorator(True)
def check_negation():
    return True

if __name__ == '__main__':
    result = check_negation()
    print(result)