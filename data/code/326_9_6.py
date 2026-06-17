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
        def wrapper(*f_args, **f_kwargs):
            result = func(*f_args, **f_kwargs)
            return result
        return wrapper
    def log_average(*args, **kwargs):
        results = []
        for _ in range(3):
            try:
                res = func(*args, **kwargs)
                results.append(res)
            except Exception as e:
                print(f"Error during execution: {e}")
        if results:
            average = sum(results) / len(results)
            print(f"Average of function results: {average}")
    return log_average
@average_logger
def calculate_sum(a, b):
    return a + b
@average_logger
def multiply(x, y):
    return x * y
if __name__ == '__main__':
    print("Testing calculate_sum:")
    calculate_sum(10, 5)
    calculate_sum(20, 3)
    calculate_sum(1, 1)
    print("-" * 20)
    print("Testing multiply:")
    multiply(2, 4)
    multiply(5, 2)
    multiply(10, 1)