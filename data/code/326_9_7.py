import functools
def average_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    @functools.wraps(func)
    def after_call(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    @functools.wraps(func)
    def wrapper_with_logging(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (list, tuple)):
            average = sum(result) / len(result)
            print(f"--- Logging for {func.__name__} ---")
            print(f"Results: {result}")
            print(f"Average: {average}")
            print("------------------------------")
        else:
            print(f"--- Logging for {func.__name__} ---")
            print(f"Result: {result}")
            print("No average calculated (result is not a list or tuple).")
            print("------------------------------")
        return result
    return wrapper_with_logging
def calculate_average(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (list, tuple)):
            average = sum(result) / len(result)
            print(f"--- Logging for {func.__name__} ---")
            print(f"Results: {result}")
            print(f"Average: {average}")
            print("------------------------------")
        else:
            print(f"--- Logging for {func.__name__} ---")
            print(f"Result: {result}")
            print("No average calculated (result is not a list or tuple).")
            print("------------------------------")
        return result
    return wrapper
@calculate_average
def sum_of_numbers(a, b):
    return [a + b, a * b]
@calculate_average
def multiply_list(nums):
    return [x * 2 for x in nums]
if __name__ == '__main__':
    print("Testing sum_of_numbers:")
    sum_of_numbers(10, 5)
    print("\nTesting multiply_list:")
    multiply_list([1, 2, 3])