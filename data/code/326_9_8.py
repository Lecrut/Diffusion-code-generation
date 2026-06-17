import functools
def average_log(func):
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
@average_log
def calculate_sum(a, b):
    return [a + b, a * b]
@average_log
def get_numbers(nums):
    return nums
if __name__ == '__main__':
    print("--- Testing calculate_sum ---")
    sum_result = calculate_sum(10, 5)
    print(f"Returned value: {sum_result}\n")
    print("--- Testing get_numbers ---")
    numbers_result = get_numbers([1, 2, 3, 4])
    print(f"Returned value: {numbers_result}\n")