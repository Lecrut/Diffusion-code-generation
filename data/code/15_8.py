def match_checker(expected_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result != expected_value:
                raise AssertionError(f"Expected {expected_value}, but got {result}")
            return result
        return wrapper
    return decorator
@match_checker(42)
def get_answer(a, b):
    return a + b
if __name__ == '__main__':
    try:
        result = get_answer(20, 22)
        print(f"Result: {result}")
    except AssertionError as e:
        print(f"Error: {e}")