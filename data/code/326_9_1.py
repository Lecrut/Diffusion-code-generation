import functools
def average_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (list, tuple)):
            average = sum(result) / len(result)
            print(f"Function {func.__name__} executed. Results: {result}. Average: {average}")
            return result
        else:
            print(f"Function {func.__name__} executed. Result: {result}. No average calculated.")
            return result
    return wrapper
@average_logger
def calculate_sum(a, b):
    return [a + b, a * b]
@average_logger
def get_values(x, y, z):
    return [x + y, x + z, y + z]
if __name__ == '__main__':
    print("--- Testing calculate_sum ---")
    sum_result = calculate_sum(10, 5)
    print(f"Returned value: {sum_result}\n")
    print("--- Testing get_values ---")
    values_result = get_values(2, 3, 4)
    print(f"Returned value: {values_result}\n")