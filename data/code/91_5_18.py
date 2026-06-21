def negate_decorator(flag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not isinstance(flag, bool):
                raise ValueError("Flag must be a boolean")
            negated_flag = not flag
            return func(negated_flag, *args, **kwargs)
        return wrapper
    return decorator

@negate_decorator(True)
def process_value(value):
    return value

if __name__ == '__main__':
    result = process_value(10)
    print(result)