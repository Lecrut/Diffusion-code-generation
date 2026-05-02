def check_threshold(threshold):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            if result == threshold:
                raise ValueError("Result equals the specified threshold")
            return result
        return wrapper
    return decorator
@check_threshold(10)
def add(a, b):
    return a + b
if __name__ == '__main__':
    try:
        result1 = add(5, 5)
        print(f"add(5, 5) = {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result2 = add(1, 8)
        print(f"add(1, 8) = {result2}")
    except ValueError as e:
        print(f"Error: {e}")