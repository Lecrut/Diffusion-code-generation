def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes if 'condition' is True.
    
    Args:
        condition (bool or any truthy value): The initial state checked before execution.
        
    Returns:
        Decorated callable
    
    Raises:
        TypeError: If the passed condition cannot be evaluated as boolean-like.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not bool(condition):
                print(f"Execution blocked because check_truth was called with {condition!r} (not truthy).")
                return None
            
            result = func(*args, **kwargs)
            
            # Optional: Update state after successful execution? 
            # For this implementation, the condition is evaluated only once at decoration time.
            # If dynamic updates are needed based on arguments, a different design pattern would be required.
            return result
        
        return wrapper
    
    return decorator

# Example usage block
if __name__ == '__main__':
    def add_numbers(a, b):
        """Adds two numbers and returns the sum."""
        print(f"Calculating {a} + {b}")
        return a + b

    # Scenario 1: Condition is True (truthy) - Function executes
    @check_truth(True)
    def execute_when_true():
        print("This block executed because condition was truthy.")
    
    result_1 = execute_when_true()