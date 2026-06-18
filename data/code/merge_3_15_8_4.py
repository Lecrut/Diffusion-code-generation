import functools

# Predefined constant value to match against
TARGET_VALUE = 42

def match_checker(target_value: int) -> callable:
    """
    Decorator that wraps a function and checks if its result matches the target_value.
    
    Args:
        target_value (int): The integer value that the decorated function's output must equal.

    Returns:
        callable: A wrapper function that executes the original function and prints 
                  whether it matched or failed to match the target. If no exception is raised,
                  it implies successful execution regardless of result matching behavior below unless specified otherwise.
    
    Note on Logic:
        The decorator captures the return value but does not alter normal flow (i.e., doesn't raise errors internally)
        as typically decorators are used for side effects like logging or validation reporting post-execution. 
        However, since the prompt asks to "check if... matches", we will perform this check inside the wrapper and print status.
    """
    
    @functools.wraps(lambda: None)  # Preserve original name/function metadata loosely as decorator signature doesn't allow direct access without inspecting args fully yet
    
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if isinstance(result, int) and target_value == result:
                print(f"SUCCESS: Result {result} matches the expected value {target_value}.")
            else:
                print(f"MISMATCH: Got {result}, but expected {target_value}.")
            
            return result
        
        return inner
    
    # Bind decorator to accept a function dynamically? 
    # Actually, standard Python decorators apply at decoration time. We must structure it so that 'match_checker' itself is the callable we define now with target as arg.
    
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if isinstance(result, int) and result == TARGET_VALUE:
                print(f"SUCCESS: Result {result} matches the expected value {TARGET_VALUE}.")
            else:
                print(f"MISMATCH: Got {result}, but expected {TARGET_VALUE}.")
            
            return result
        
        return inner
    
    # Re-evaluating structure because 'match_checker(target_value)' should be a decorator factory if target varies, 
    # OR it could just take the function and hardcode inside? The prompt says "accepts a function". It implies single use per definition scope or variable capture.
    
    # Let's redefine to make match_checker itself accept both: func and value? No, syntax is `@match_checker`.
    # So @match_checker must be callable with (func). Where does the 'value' come from? 
    # The prompt says "matches a predefined constant value". This implies we can use globals or pass it. 
    # Let's assume the decorator factory pattern where match_checker is called once, but since Python allows passing variables to decorators if they are in scope when defined:
    
    return inner  # Wait, this returns 'inner' directly? No, that breaks syntax for @match_checker(func).
    
    pass

# Correct Structure Implementation

def make_matcher(target):
    """Factory function. But the prompt asks for a decorator named `@match_checker`. 
    Usually decorators are functions returning wrappers. If match_checker takes (func), it must have access to target."""
    
    # Since we need global constant 'TARGET_VALUE', let's use that directly in the wrapper logic if passed as arg or captured?
    # To allow @match_checker(func) where func returns int, and checks against TARGET_VALUE defined globally:

def match_checker(target_value):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if isinstance(result, int) and target_value == result:
                print(f"SUCCESS: Result {result} matches the expected value {target_value}.")
            else:
                print(f"MISMATCH: Got {result}, but expected {target_value}.")
                
            return result
        
        return wrapper
    
    # Wait, if I define `def match_checker(target_value):` and call it as @match_checker(func), 
    # then 'func' becomes the first argument? No. Python decorators are called like: decorator(func).
    # So if I write @match_checker(val) -> this calls match_checker(val) which returns a decorator function that takes func.
    
    return decorator

# But wait, standard usage is:
# result = 42
# def foo(): ...
# @decorator(result)
# def bar(): pass
    
# The prompt says "accepts a function". It does not explicitly say it accepts the value as argument in syntax like `@match_checker(val, func)`? 
# Usually decorators are single line: @dec. If we want to check against a constant, and that constant is global (TARGET_VALUE),
# then match_checker can just accept 'func'.

def simple_matcher(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # Check against the predefined constant TARGET_VALUE defined in this module scope
        if isinstance(result, int) and target_value == result:
            print(f"SUCCESS: Result {result} matches the expected value {target_value}.")
        else:
            print(f"MISMATCH: Got {result}, but expected {TARGET_VALUE}.")
            
        return result
    
    return wrapper

# Actually, re-reading carefully: "accepts a function and returns a wrapper... check if ... matches a predefined constant".
# If the decorator is applied as `@match_checker`, it only gets one argument (the function). 
# How does it know what value to match against? It must use the global TARGET_VALUE.

def match_checker(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        # Check if result matches predefined constant TARGET_VALUE
        if isinstance(result, int) and result == TARGET_VALUE:
            print(f"SUCCESS: Result {result} matches the expected value {TARGET_VALUE}.")
        else:
            print(f"MISMATCH: Got {result}, but expected {TARGET_VALUE}.")
            
        return result
    
    return wrapper

if __name__ == '__main':
    def my_function():
        # Simulate a function that returns 42 (the constant)
        return TARGET_VALUE

    decorated_func = match_checker(my_function)
    
    @decorated_func
    def run_test():
        print("Running test...")
        val = 10 + 32
        
        if isinstance(val, int):
            # Just to ensure logic holds for another value too? 
            # But let's stick to the specific request: check against TARGET_VALUE.
            pass
            
    run_test()

# Wait, I need to make sure the syntax `@match_checker` works directly with my_function or if it requires an argument like @match_checker(func)?
# The prompt says "accepts a function". So yes, one arg. 
# If I use global TARGET_VALUE, then:

if __name__ == '__main__':
    pass
