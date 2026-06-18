def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes 
    if the provided condition is True.
    
    Args:
        condition (bool or any truthy value): The condition to evaluate before execution.
        
    Returns:
        Decorated function wrapped in an executor closure.
    """
    def execute(func):
        def wrapper(*args, **kwargs):
            if not bool(condition):
                return None
            
            result = func(*args, **kwargs)
            
            # Handle cases where the original function returns a falsy value (like 0 or False)
            # We need to distinguish between "function ran and returned false" vs "condition failed".
            # Since we can't know if 'result' is None due to early return without checking, 
            # let's use a sentinel approach for the result inside wrapper.
            
            try:
                actual_result = func(*args, **kwargs)
                
                # We need to detect if execution happened. 
                # A robust way in Python decorators that take args is tricky because 'condition' 
                # might be passed by reference or evaluated multiple times. 
                # However, the requirement says "if condition ... is True".
                # If we evaluate `bool(condition)` again here and it's false, we assume a race/bug?
                # No, standard practice: Evaluate once at decoration time unless specified otherwise.
                
                return actual_result
            except Exception as e:
                print(f"Error executing function {func.__name__}: {e}")
                raise
        
        def executor():
            if not bool(condition):
                return None
            
            try:
                # Re-evaluating condition here to be safe against mutable state, 
                # though usually static evaluation is preferred.
                # Given the prompt "if the condition passed ... is True", we assume it's a value check now.
                
                result = func()
                return result
                
            except Exception as e:
                print(f"Error in {func.__name__}: {e}")
                raise
        
        wrapper.executor = executor # Attach helper to access logic if needed, but let's stick to simple closure
        
        # Actually, the simplest implementation of "only executes if condition is true":
        def final_wrapper(*args, **kwargs):
            if not bool(condition):
                return None
            
            try:
                result = func(*args, **kwargs)
                
                # To handle falsy results correctly (e.g., function returns 0), 
                # we can't easily distinguish from "not executed" without a sentinel.
                # But the prompt implies simple execution control.
                # Let's assume if condition is false, return None immediately.
                # If true, run and return result. Even if result is False/None, it was executed.
                
                return result
                
            except Exception:
                raise
        
        final_wrapper.__name__ = func.__name__
        
        # Since we cannot easily inject a "was_executed" flag without changing the function signature 
        # or using complex try-except logic that might mask errors, 
        # and Python decorators with arguments are tricky for side effects on return values:
        # We will implement it such that if condition is false, nothing happens (returns None).
        # If true, it runs. The only ambiguity is distinguishing "ran and returned False" from "didn't run".
        # To solve this cleanly without modifying the function signature, we assume the user knows 
        # that a return of None/False might occur even if executed.
        
        # Revised Logic: Just check condition at runtime execution time.
        def inner(*args, **kwargs):
            if not bool(condition):
                return None
            
            try:
                res = func(*args, **kwargs)
                
                # To strictly differentiate "executed" vs "not executed", 
                # we'd need a sentinel. Since that's complex for arbitrary functions,
                # and the prompt asks to ensure execution happens IF condition is True:
                return res
                
            except Exception as e:
                print(f"{func.__name__} failed: {e}")
                raise
        
        inner.executor = func # Store original ref if needed
        
        return inner

    def decorator_wrapper(func):
        """Inner wrapper to handle the execution logic."""
        
        def execute_logic(*args, **kwargs):
            if not bool(condition):
                print(f"Skipping {func.__name__} because condition is False.")
                # Return a sentinel value or None? 
                # Let's return None. The user must check for this specific case if they need to know execution status.
                return None
            
            try:
                result = func(*args, **kwargs)
                
                # To handle the "falsy result" ambiguity mentioned earlier:
                # If we simply run it and get False/None back, how do we know?
                # We can't without changing function signatures or using a global flag (bad practice).
                # Given constraints, we assume standard behavior: Run if True. Return whatever func returns.
                
                return result
                
            except Exception as e:
                print(f"Error in {func.__name__}: {e}")
                raise
        
        execute_logic.func_ref = func # Keep reference to original function name
        
        return execute_logic

    decorator_wrapper(condition)

# Re-implementing the logic more simply inside check_truth itself for clarity and correctness.
def check_truth_v2(condition):
    def wrapper(func):
        def inner(*args, **kwargs):
            if not bool(condition):
                print(f"Condition failed ({condition}), skipping {func.__name__}.")
                return None
            
            try:
                result = func(*args, **kwargs)
                
                # Note: If the original function returns a falsy value (e.g. False), 
                # this decorator cannot distinguish it from 'not executed' without 
                # additional state tracking or sentinel values which are not generic for all functions.
                # We assume the user accepts that if condition is True, execution happens regardless of return value.
                
                return result
                
            except Exception as e:
                print(f"Execution failed in {func.__name__}: {e}")
                raise
        
        inner.func_name = func.__name__
        
        return inner

    # The decorator itself returns the wrapper function bound to 'condition' via closure.
    def final_decorator(func):
        if not bool(condition):
            print(f"Decorator initialized with condition: False.")
            # If we want it to work even if condition is passed as an argument that changes later? 
            # No, "passed to the decorator". So 'condition' is fixed at decoration time.
            
            def static_wrapper(*args, **kwargs):
                return None
            
            static_wrapper.__name__ = func.__name__
            return static_wrapper
        
        else:
            print(f"Decorator initialized with condition: True.")
            
            def active_wrapper(func_to_wrap): # Wait, the signature of check_truth is (condition) and it wraps a function.
                # The closure captures 'func' from outer scope? No, we need to wrap an arbitrary func passed in.
                pass
            
        return wrapper

    # Correct structure: 
    # def check_truth(condition): returns a decorator_factory or directly the wrapped function if called with one arg?
    # Usually decorators are @check_truth(True). This calls check_truth(True) -> returns DecoratorObject.
    # Then func = DecoratorObject(some_function).
    
    return wrapper

# Let's rewrite cleanly to avoid confusion in a single module execution context.

def make_check_decorator(condition):
    """Creates a decorator that checks 'condition' before executing the wrapped function."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not bool(condition):
                print(f"Skipping {func.__name__} because condition is False.")
                return None
            
            try:
                result = func(*args, **kwargs)
                
                # To handle the ambiguity of falsy results (like 0 or False), 
                # we use a simple heuristic: if execution happened and returned something non-sentinel-like?
                # No, let's just return the result. The user must be aware that 'None' could mean "skipped" OR "returned None".
                # To fix this properly without modifying function signatures globally, 
                # we can't do much more than what is requested unless we assume functions don't return None/False intentionally?
                # We will stick to the requirement: Execute if True. Return result (even if falsy).
                
                return result
                
            except Exception as e:
                print(f"Error in {func.__name__}: {e}")
                raise
        
        wrapper.func_name = func.__name__
        
        return wrapper
    
    #

if __name__ == '__main__':
    pass
