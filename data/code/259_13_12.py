def log_extremes(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Input: {args}, {kwargs}")
        print(f"Output: {result}")
        return result
    return wrapper

@log_extremes
def find_max_value(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_value = max(numbers)
    return max_value

if __name__ == '__main__':
    sample_list = [3.14159, 1.61803, 2.71828, -0.57721, 100.0, -5.2]
    try:
        max_val = find_max_value(sample_list)
        print(f"The maximum element in the list is: {max_val}")
    except ValueError as e:
        print(e)