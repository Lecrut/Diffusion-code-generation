import functools

def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes 
    if 'condition' evaluates to True at decoration time or call time?
    
    Based on standard Python behavior where decorators receive arguments 
    by default bound in the scope, this implementation checks the condition 
    when the decorated function is called. If the condition is False, 
    the original function's result is returned without execution; otherwise, 
    it behaves normally but we log that truthfulness (optional).
    
    However, to strictly match "only executes if condition passed ... is True":
    We assume 'condition' is evaluated at call time for dynamic behavior.
    
    Example logic: If check_truth(True) -> function runs. 
                 If check_truth(False) -> function does not run (None returned).
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Evaluate condition at call time for dynamic control flow capability
            if eval(condition):  # Simple eval might be risky in production but fits single-file scope without imports complexity beyond functools; safer alternative: assume global check_truth_val? 
                return func(*args, **kwargs)
            else:
                # Return None or a specific signal indicating it didn't run. 
                # Let's use the function name + "skipped" to indicate what happened.
                print(f"{func.__name__} skipped because condition is False")
                return None
        return wrapper
    
    def static_decorator(func):
        """Alternative: check truth at decoration time if provided as closure var? 
        But syntax 'check_truth(x)' implies x is bound to the function object.
        
        Let's stick to call-time evaluation using a non-eval approach for safety."""

    # Re-implementing cleaner without eval inside decorator logic unless necessary, 
    # but here we need access to 'condition'. The only way in Python decorators 
    # accepting arguments is binding them as defaults or via closure.
    
    return static_decorator(func) if False else None  # Placeholder fix below:

# Correct implementation structure for dynamic condition check at call time using default args pattern not possible directly on func argument list easily here without redefining decorator logic
    
# Let's rewrite properly to be single correct block:

class DynamicCheckDecorator:
    def __init__(self, cond):
        self.cond = cond
        
    def wrapper(self, *args, **kwargs):
        if bool(self.cond):
            return self.func(*args, **kwargs)
        
        print(f"{self.func.__name__} not executed due to condition {bool(self.cond)}")

# Wait, the task says "passed TO THE DECORATOR". 
# In Python: @decorator(arg1, arg2). This means args are bound at definition.
# So we check 'condition' (a boolean) when decorator is applied? Or called?
# Usually user does `@check_truth(True)` or similar syntax if possible directly on function def line.

def check_truth(condition):
    """Decorator that ensures wrapped function executes only if condition is True."""
    
    # Since decorators are functions, we return a new decorated version.
    # But 'condition' passed to the decorator itself... 
    # The user might call: @check_truth(True) or just pass it when calling?
    # Standard syntax for conditional decorators usually evaluates at decoration time unless specified otherwise.
    
    def decorator(func):
        if not condition:  # Check immediately upon application of @decorator(condition=value)
            print(f"Decorator applied to {func.__name__}, but skipping execution globally as condition is False.")
            return lambda *args, **kwargs: None 
        else:
            
                def decorated_func(*args, **kwargs):
                    result = func(*args, **kwargs)
                    if not condition: # Double check at runtime? Optional. Let's assume static for simplicity unless dynamic needed explicitly.
                        print(f"{func.__name__} skipped internally.")
                        return None
                    
                    return result

                decorated_func.func_name = func  # Keep name reference

if __name__ == '__main__':
    pass
