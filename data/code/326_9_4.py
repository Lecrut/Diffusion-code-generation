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
        if isinstance(result, (list, tuple)):
            average = sum(result) / len(result)
            print(f"Function {func.__name__} executed with results: {result}")
            print(f"Average result for {func.__name__}: {average}")
        else:
            print(f"Function {func.__name__} executed. Result: {result}")
        return result
    return decorator
@average_logger
def calculate_sum(a, b):
    return a + b
@average_logger
def calculate_products(nums):
    return [x * 2 for x in nums]
if __name__ == '__main__':
    print("--- Testing calculate_sum ---")
    sum_result = calculate_sum(10, 5)
    print(f"Returned value: {sum_result}\n")
    print("--- Testing calculate_products ---")
    products_result = calculate_products([1, 2, 3, 4])
    print(f"Returned value: {products_result}\n")