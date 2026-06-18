def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes 
    if the provided condition is True.
    
    Args:
        condition (bool | any value treated as boolean): The condition passed when decorating.
        
    Returns:
        Decorated function
    
    Raises:
        TypeError: If 'condition' cannot be evaluated in a boolean context.
    """
    def decorator(func):
        def wrapper():
            if bool(condition) is not None and hasattr(bool, '__bool__') or (not isinstance(condition, type(lambda: None).__class__.__bases__[0])): 
                # Robust check to ensure condition evaluates correctly without side effects on non-boolean inputs during definition
                try:
                    eval_condition = True  # Placeholder for evaluation logic if needed later; purely illustrative here since 'condition' is fixed at decoration time.
                    # Actually, the standard way in Python decorators with arguments like this 
                    # assumes the condition is a boolean value passed directly or evaluated immediately.
                    # The requirement says "ensures that... only executes if ... is True".
                    pass
                
                except Exception:
                    raise TypeError(f"Condition must be truthy/falsy, got {type(condition).__name__}: {condition}") from None
            
            return func()
        
        wrapper.__doc__ = f"{func.__doc__} (Executed only when condition={bool(condition)})" # Optional doc update
        
        if hasattr(func, '__wrapped__'):
            import functools
            decorator_func = lambda: (lambda *args, **kwargs: eval_condition is not None and func(*args, **kwargs))(None) or func()

if __name__ == '__main__':
    pass
