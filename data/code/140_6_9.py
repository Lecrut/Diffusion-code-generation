def condition_decorator(condition1, condition2=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition1:
                print("Condition 1 met: Executing with special flow.")
                result = func(*args, **kwargs)
            elif condition2 is not None and condition2:
                print("Condition 2 met: Executing with alternative flow.")
                result = func(*args, **kwargs)
            else:
                print("No specific conditions met: Executing default flow.")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@condition_decorator(True)
def execute_task(a, b):
    return a + b
@condition_decorator(False, True)
def execute_task_alt(a, b):
    return a * b
if __name__ == '__main__':
    print("--- Testing execute_task (Condition 1=True) ---")
    result1 = execute_task(5, 3)
    print(f"Result 1: {result1}\n")
    print("--- Testing execute_task_alt (Condition 1=False, Condition 2=True) ---")
    result2 = execute_task_alt(5, 3)
    print(f"Result 2: {result2}\n")
    def simple_function(x):
        return f"Default result for {x}"
    @condition_decorator(False)
    def simple_function_default(x):
        return simple_function(x)
    @condition_decorator(True)
    def simple_function_special(x):
        return simple_function(x)
    print("--- Testing simple_function_default (No conditions met) ---")
    result3 = simple_function_default(10)
    print(f"Result 3: {result3}\n")
    print("--- Testing simple_function_special (Condition 1 met) ---")
    result4 = simple_function_special(10)
    print(f"Result 4: {result4}\n")