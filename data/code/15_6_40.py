def match_checker(expected_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result != expected_value:
                raise ValueError(f"Result {result} does not match the expected value {expected_value}")
            return result
        return wrapper
    return decorator

@match_checker(15)
def add_and_multiply(a, b, c):
    return (a + b) * c

if __name__ == '__main__':
    try:
        print(add_and_multiply(2, 3, 4))
    except ValueError as e:
        print(e)