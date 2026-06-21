def boolean_negator(negate: bool):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not isinstance(negate, bool):
                raise ValueError("negate must be a boolean")
            result = func(*args, **kwargs)
            if negate:
                return not result
            return result
        return wrapper
    return decorator

@boolean_negator(True)
def is_positive(value: int) -> bool:
    return value > 0

if __name__ == '__main__':
    result = is_positive(10)
    print(result)