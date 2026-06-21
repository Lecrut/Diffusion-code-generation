def match_checker(expected_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == expected_value:
                return result
            else:
                raise ValueError(f"Result {result} does not match the expected value {expected_value}")
        return wrapper
    return decorator

@match_checker(100)
def multiply(a, b):
    return a * b

if __name__ == '__main__':
    try:
        print(multiply(10, 10))
    except ValueError as e:
        print(e)