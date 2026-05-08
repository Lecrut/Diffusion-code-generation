def condition_decorator(condition1, condition2=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition1:
                print("Condition 1 met. Executing function normally.")
            elif condition2 is not None and condition2:
                print("Condition 2 met. Executing function with special flow.")
            else:
                print("No specific conditions met. Executing function normally.")
            result = func(*args, **kwargs)
            if condition1 and condition2:
                print("Post-execution check: Both conditions were true.")
            return result
        return wrapper
    return decorator
@condition_decorator(True, False)
def my_function(a, b):
    return a + b
@condition_decorator(False, True)
def another_function(x, y):
    return x * y
if __name__ == '__main__':
    print("--- Testing my_function (Condition 1=True, Condition 2=False) ---")
    result1 = my_function(10, 5)
    print(f"Result 1: {result1}\n")
    print("--- Testing another_function (Condition 1=False, Condition 2=True) ---")
    result2 = another_function(4, 6)
    print(f"Result 2: {result2}\n")
    @condition_decorator(True, True)
    def combined_function(p, q):
        return p * q
    print("--- Testing combined_function (Condition 1=True, Condition 2=True) ---")
    result3 = combined_function(3, 4)
    print(f"Result 3: {result3}\n")