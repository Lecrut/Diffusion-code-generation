def condition_decorator(condition1=False, condition2=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition1:
                print("Condition 1 met: Executing early path.")
                return None
            elif condition2:
                print("Condition 2 met: Executing alternative path.")
                return "Alternative Result"
            else:
                print("Default path: Executing original function.")
                return func(*args, **kwargs)
        return wrapper
    return decorator
@condition_decorator(condition1=True, condition2=False)
def my_function(a, b):
    result = a + b
    print(f"Inside my_function: {result}")
    return result
@condition_decorator(condition1=False, condition2=True)
def another_function(x, y):
    result = x * y
    print(f"Inside another_function: {result}")
    return result
if __name__ == '__main__':
    print("--- Testing my_function (condition1=True, condition2=False) ---")
    result1 = my_function(5, 3)
    print(f"Final result from my_function: {result1}\n")
    print("--- Testing another_function (condition1=False, condition2=True) ---")
    result2 = another_function(4, 5)
    print(f"Final result from another_function: {result2}\n")
    print("--- Testing a case where neither condition is met (requires re-defining a function for this specific test) ---")
    @condition_decorator(condition1=False, condition2=False)
    def default_function(a, b):
        result = a * b
        print(f"Inside default_function: {result}")
        return result
    result3 = default_function(6, 7)
    print(f"Final result from default_function: {result3}")