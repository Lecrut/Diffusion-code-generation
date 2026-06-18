def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes 
    if 'condition' is True. If condition is False, the wrapped 
    function will not run and its return value will be None.
    
    Args:
        condition (bool or any truthy/falsy value): The condition to check.
        
    Returns:
        Decorated function that executes only when condition evaluates to True.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not bool(condition):
                return None
            
            result = func(*args, **kwargs)
            
            # If the original function returns a falsy value (like 0 or False),
            # we still consider it executed successfully. However, to strictly 
            # adhere to "only execute if condition is True", this wrapper ensures execution happens.
            # The return value of func itself doesn't affect whether it ran here.
            
            return result
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    # Example usage with hard-coded sample values
    
    @check_truth(True)  # Condition is True, function should execute
    def add_numbers(a, b):
        """Adds two numbers and returns the sum."""
        print(f"Adding {a} + {b}")
        return a + b

    @check_truth(False)  # Condition is False, function should NOT execute
    def multiply_by_zero(x):
        """Multiplies x by zero (should not run)."""
        print("This line will never be printed.")
        return x * 0

    @check_truth(1 == 2)  # Condition evaluates to False, function should NOT execute
    def greet(name):
        """Greets a person."""
        print(f"Hello {name}!")
        return f"Greeting for {name}"

    print("Running functions with True condition:")
    result = add_numbers(5, 10)
    print(f"Result: {result}\n")

    print("Running function with False condition (should be skipped):")
    # Note: multiply_by_zero and greet are decorated to NOT run because their conditions are false.
    
    @check_truth(True)  # Re-decorating for demonstration of a working case after the first block logic
    def safe_operation(flag=True):
        """Safe operation that runs if flag is True."""
        print("Operation executed successfully.")
        return "Success"

    result = safe_operation()
    print(f"Safely Operation Result: {result}")