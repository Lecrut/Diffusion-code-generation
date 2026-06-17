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
            print(f"Function {func.__name__} executed with results: {result}")
            print(f"Average of results for {func.__name__}: {average}")
        else:
            print(f"Function {func.__name__} executed. Result: {result}")
        return result
    return wrapper_with_logging
if __name__ == '__main__':
    @average_logger
    def calculate_sum(a, b):
        return [a + b, a * b]
    @average_logger
    def get_values(x, y, z):
        return [x, y, z]
    print("--- Testing calculate_sum ---")
    sum_result = calculate_sum(10, 5)
    print(f"Returned value: {sum_result}\n")
    print("--- Testing get_values ---")
    values_result = get_values(1, 2, 3)
    print(f"Returned value: {values_result}\n")