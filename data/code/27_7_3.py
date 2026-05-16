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
def calculate_difference(a, b):
    return a - b
if __name__ == '__main__':
    val1 = 20
    val2 = 10
    try:
        diff = calculate_difference(val1, val2)
        print(f"Difference between {val1} and {val2}: {diff}")
    except ValueError as e:
        print(f"Error: {e}")
    val3 = 10
    val4 = 10
    try:
        diff = calculate_difference(val3, val4)
        print(f"Difference between {val3} and {val4}: {diff}")
    except ValueError as e:
        print(f"Error: {e}")