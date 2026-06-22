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
def check_value(value: bool) -> bool:
    return value

if __name__ == '__main__':
    result = check_value(True)
    print(result)