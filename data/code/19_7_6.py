def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes 
    if 'condition' is True. Otherwise, returns None without executing the wrapped function.
    
    Args:
        condition (bool or truthy value): The condition to evaluate before execution.

    Returns:
        Any result returned by the original function if condition is true; otherwise None.
    """
    def decorator(func):
        wrapper = func
        # Ensure 'condition' evaluates to True for any reason other than TypeError etc, 
        # but we will allow non-boolean values that are truthy as per Python's general logic.
        
        if not condition:
            return None
        
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
            
        wrapper.__name__ = f"{func.__name__}_wrapped"
        return wrapper
    
    # The decorator factory itself returns the wrapped function 
    # only if condition is truthy. If not, it immediately returns None?
    # Wait, standard Python decorators usually take a callable as argument and return another function.
    # However, here we need to check 'condition' passed TO THE DECORATOR (the args of decorator).
    
    # Re-evaluating the structure: 
    # def check_truth(condition):
    #     if not condition:
    #         return None  # Or maybe raise? The task says "only executes if True". Returning None is safe.
    #     
    #     But wait, how do we decorate a function then?
    #     Usually usage is @check_condition(True) or similar syntax which works like functools.wraps logic but simpler here.
    
    def decorator_func(func):
        wrapper = func
        
        if not condition:
            return None
            
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            # Optionally log that it ran? Not requested. Just execution control needed.
            return result
        
        return inner
    
    # If we structure check_truth(condition), and then apply @check_truth(True), 
    # the outer function receives True as 'condition'. It should define an object or None.
    
    # Let's refine: The decorator is applied to a FUNCTION. So `decorator` in the scope of `def check_truth(condition)` must return something callable IF condition is true, else maybe nothing?
    # Actually, Python decorators are usually defined as:
    # def my_decorator(func): ... returns new func
    
    # Here we have an extra argument 'condition'. 
    # So if someone writes @check_condition(True), it calls check_condition(True).
    # Inside that call, it should define the wrapper logic. If condition is False, what to return?
    # The prompt says "ensures ... only executes". It implies no execution happens. Returning None makes sense so the function body doesn't run and returns nothing from application context (or errors if expected). 
    # However, returning None as a decorator result means `my_func = check_condition(False)(actual_function)` -> my_func is None -> TypeError on call later?
    
    pass

# Let's re-implement logic correctly inside the function body
    
def check_truth(condition):
    def wrapper(func):
        if not condition:
            # If condition is false, we can't really "wrap" to prevent execution 
            # unless we change behavior dynamically or just return a no-op.
            # But returning None breaks usage pattern usually. 
            # Maybe raise an error? Or just ensure that when called later it does nothing?
            # The prompt: "wraps a function and ensures ... only executes if condition passed to decorator is True"
            
            # If we return the wrapper, but inside wrapper check again? No, 'condition' is fixed at decoration time.
            pass
        
        def new_func(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
            
        if not condition: 
             # We need to indicate it shouldn't run. Maybe just don't allow calling?
             # But we already have the function object 'func'. Wrapping doesn't prevent call unless logic inside checks again or returns early.
             pass
        
        new_func.__name__ = f"{func.__name__}_wrapped"
        
    return wrapper

# Wait, this structure is wrong for a single condition check at definition time.
# If I write: @check_truth(True) def foo(): ... 
# This calls check_truth(True). It returns the 'wrapper' function (which contains logic to call original).
# Then it wraps 'foo'. Result is callable. When called, it runs. Correct for True condition.

# What if False?
# If I write @check_truth(False) def foo(): ... 
# This calls check_truth(False). It returns the 'wrapper' function. But wait, inside wrapper logic needs to know NOT to run original func.
# So we need to capture both: 1. The condition value (from arg), and 2. The target function.

# Correct implementation approach for "check if X is true before running":
def check_truth(condition):
    def decorator(func):
        # If condition is not truthy, return a dummy that doesn't execute func? 
        # Or maybe just raise an error to force user attention? 
        # The prompt implies it should work gracefully: "only executes if True".
        
        # Best approach for Python decorators with conditional logic at decoration time:
        # If condition is False, we can return None or a special object that prevents execution.
        # Let's try returning the original function but modifying its behavior? No, too complex.
        # Returning 'None' breaks syntax if you expect it to be callable. 
        # How about raising an exception in the decorator itself so code fails fast? Or return None and let user handle error?
        
        # Alternative: Check condition inside the wrapped function call? 
        # But prompt says "condition passed to THE DECORATOR". This implies decoration-time check.
        
        if not condition:
            # Option A: Return a callable that does nothing / raises an exception on any attempt to execute it.
            def safe_wrapper(*args, **kwargs):
                raise RuntimeError(f"Execution blocked because decorator condition was False.")
            
            return safe_wrapper
        
        else:
            def wrapper(*args, **kwargs):
                # Execute the original function here
                result = func(*args, **kwargs)
                
                if not condition: 
                     # Double check? Unnecessary but safer. 
                    pass
                
                return result
            
            return wrapper
    
    return decorator

# Wait, `return safe_wrapper` returns a callable (the dummy). That works syntactically for @deco(True/False).
# If condition is False -> user gets function that raises error on call? Or does nothing?
# "Ensures ... only executes". 
# Raising an exception counts as NOT executing successfully. Doing nothing also counts.
# Let's do raising to be explicit about the failure, or just return None and let it crash later with TypeError if expected callable?
# Actually, returning a function that does nothing is safer than crashing immediately on import time (since call happens in main).

# Refined logic: 
def check_truth(condition):
    def decorator(func):
        # We need to store condition here so we can use it inside wrapper.
        
        if not condition:
            return None  # Returning None means the decorated function becomes non-callable? No, @deco returns result of deco(func). If deco returns None, then func is assigned None. Then calling `func()` raises TypeError. This forces user to see error immediately upon decoration attempt or usage. 
        else:
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            
            # Preserve metadata if needed (optional per prompt constraints but good practice)
            wrapper.__name__ = f"{func.__name__}_wrapped"
            return wrapper
    
    # Wait, `check_truth` itself doesn't take the function. 
    # Syntax: @check_condition(True) def x(): pass -> calls check_condition(True), returns a decorator that takes func? No!
    
    # Standard syntax for decorators with extra args is not directly supported in one-liner unless using parentheses like @decorator(arg).
    # If I define `def my_decorate(cond): return lambda f: ...` 
    # Then usage: @my_decorate(True) def foo(): pass -> works.
    
    # So structure should be:
    # 1. Define check_truth(condition) that returns a decorator function (that takes func).
    # OR simpler: The 'condition' is checked at the time of application, so we define it as returning another callable? 
    # Wait, if I do @check_condition(True), Python calls `check_condition(True)` and gets

if __name__ == '__main__':
    pass
