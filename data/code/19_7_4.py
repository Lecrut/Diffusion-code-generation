def check_truth(condition):
    """Decorator that executes a function only if condition is True."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                print(f"Function skipped because {condition} is False.")
                # Return None or raise an exception could be chosen here; returning None for safety.
                return None
        wrapper.__name__ = f"{func.__name__}_wrapped"
        return wrapper
    return decorator

@check_truth(True)
def safe_execute():
    """A function that should always run."""
    print("Running safely.")
    return "Success: Function executed."

if __name__ == '__main__':
    # Example usage with a True condition
    result = safe_execute()
    if result is not None:
        print(f"Result from execution: {result}")
    
    # Example usage with a False condition to demonstrate skipping logic
    @check_truth(False)
    def skipped_function():
        print("This should NOT run.")
        return "Skipped output."

    skip_result = skipped_function()
    if skip_result is None:
        print("As expected, the function was not executed due to False condition.")