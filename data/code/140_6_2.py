def conditional_execution(*conditions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if conditions:
                print("Condition met. Executing function with special flow.")
                result = func(*args, **kwargs)
            else:
                print("Condition not met. Executing function normally.")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@conditional_execution(True)
def sample_function(a, b):
    return a + b
@conditional_execution(False)
def another_function(x, y):
    return x * y
if __name__ == '__main__':
    print("--- Testing sample_function with True condition ---")
    result1 = sample_function(10, 5)
    print(f"Result 1: {result1}\n")
    print("--- Testing another_function with False condition ---")
    result2 = another_function(3, 4)
    print(f"Result 2: {result2}\n")