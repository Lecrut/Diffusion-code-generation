def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes 
    if 'condition' is True at decoration time (or call time depending on implementation).
    
    Since Python decorators are evaluated when the module loads, we can use an immutable condition.
    However, to make this useful for runtime checks without re-decorating, 
    a common pattern is to pass the condition as part of the decorator arguments or closure.
    
    Here, we implement it such that the function inside executes only if 'condition' evaluates to True immediately upon decoration call.
    If you need dynamic checking per call, passing the condition into the decorated function signature would be required instead.

    Note: This implementation checks truthiness at the time of application (decoration).
    """
    def decorator(func):
        # The check happens here when the decorator is applied to a function
        if not condition:
            return func  # Return original but perhaps warn or skip execution logic? 
                         # Actually, per task "ensures that... only executes", returning early means it won't run.
                         # But we want to execute normally IF true. So let's just wrap and check inside the wrapper call too?
        else:
            def wrapped(*args, **kwargs):
                return func(*args, **kwargs)
            
            # To satisfy "only executes if condition is True", we can simply not run it at all if False.
            # But usually decorators are applied once. Let's assume the user wants to know 
            # that this specific decorated function will only ever be called in a context where condition was true?
            # Or perhaps they want dynamic checking inside the wrapper?
            
            # Re-reading: "ensures that the wrapped function only executes if the condition passed... is True"
            # If I apply @check_truth(False), it should never run. 
            # If I apply @check_truth(True), it runs normally.
            return func
        
        def wrapper(*args, **kwargs):
            print(f"Warning: Condition {condition} was False at decoration time.")
            # We can't easily prevent execution if the user calls it later unless we don't execute anything?
            # But the task says "only executes". 
            # Let's interpret this as: The wrapper function body should not run its main logic.
            
            return None
        
        return wrapper

    # Actually, a better interpretation for Python decorators that are static at import time:
    # If condition is False, we might just skip wrapping or wrap in a no-op.
    # But if the user wants dynamic checking (e.g., check_truth(True)) they'd pass True? 
    # Let's implement it such that the wrapper checks 'condition' again on every call for maximum safety,
    # OR simpler: Since decorators are evaluated at import time, we can just return a function that does nothing if False.

    # Revised approach to meet "only executes":
    def final_wrapper(*args, **kwargs):
        nonlocal condition
        if not condition:
            print(f"Function skipped because check_truth({condition}) is False.")
            return None
        
        result = func(*args, **kwargs)
        
        # If we want to ensure it ONLY executes when True at decoration time (static), 
        # then the above nonlocal check inside wrapper might be redundant if condition was already checked.
        # But let's stick to static evaluation for simplicity unless dynamic is implied.
        return result

    # Wait, standard decorator syntax: @check_truth(True) -> creates a function that checks True? No.
    # The argument 'condition' IS passed into the decorator factory.
    
    def inner(func):
        if condition:
            print(f"Decorator active for {func.__name__} (Condition was True)")
            return func
        
        else:
            print(f"Decorator inactive for {func.__name__} (Condition was False)")
            
            # To ensure it NEVER executes, we can just not wrap the logic or make wrapper empty.
            def never_run(*args, **kwargs):
                pass
            
            inner_func = lambda *a, **k: None if condition else func(a, k) 
            return inner_func

    # Let's simplify for clarity and correctness based on "only executes":
    
    def decorator_factory(cond_val):
        def decorator(func):
            print(f"Applying @check_truth({cond_val}) to {func.__name__}")
            
            if cond_val:
                return func
            
            else:
                # Wrap in a function that prints warning and returns None (or original result but doesn't do work?)
                # "Only executes" implies the body of 'func' is not run.
                
                def wrapper(*args, **kwargs):
                    print(f"Function {func.__name__} skipped because condition was False.")
                    return func(*args, **kwargs)  # Technically it still calls func? 
                    
                # To truly prevent execution:
                def safe_wrapper(*args, **kwargs):
                     pass
                
                # Actually, if I want to call the function but only if True... that's impossible in a static decorator.
                # The most logical interpretation for "only executes" is that the wrapper logic runs, 
                # and inside it checks condition again? Or simply doesn't invoke func at all.
                
                def final_wrapper(*args, **kwargs):
                    print(f"{func.__name__} execution prevented by check_truth({cond_val})")
                    
                return final_wrapper
        
        return decorator

    # Wait, I need to handle the argument passing correctly in Python 3 syntax @check_truth(True)
    
    def apply_decorator(func_to_decorate):
        if condition:
            print(f"Executing {func_to_decorate.__name__} as condition is True.")
            func_to_decorate()
        else:
            print(f"Not executing {func_to_decorate.__name__} as condition is False.")

    return apply_decorator

# Correct Implementation Logic for the Task Requirements:
def check_truth(condition):
    """
    Decorator that ensures a function only executes if 'condition' evaluates to True.
    
    Since decorators are applied at import time, this checks the truthiness of 
    the passed condition immediately when the decorator is invoked on a function.
    If False, it returns a wrapper that prevents execution (or logs and skips).
    """
    def decorator(func):
        # Check if we should allow execution based on the static argument 'condition'
        print(f"Decorator check: {func.__name__} with condition={condition}")
        
        if not condition:
            # If False, return a wrapper that does nothing or logs and skips calling func.
            def skip_wrapper(*args, **kwargs):
                print(f"[check_truth({condition})] Skipping execution of {func.__name__}.")
                return None
            
            return skip_wrapper
        
        else:
            # If True, just return the original function (or a trivial wrapper)
            def run_wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            
            return run_wrapper

    return decorator

if __name__ == '__main__':
    # Example usage
    
    @check_truth(True)  # Condition is True -> Function will execute
    def greet():
        print("Hello from the executed function!")
    
    @check_truth(False) # Condition is False -> Function should NOT execute logic (skipped)
    def secret_message():
        print("This message remains hidden.")

    # Simulating a dynamic scenario where we might want to check condition at runtime? 
    # The task says "condition passed to the decorator". This implies static argument.
    
    greet()      # Should run
    result = secret_message()  # Should return None and print skip warning
    
    # Additional test with explicit True/False logic inside main if needed, but decorators handle it now.