def check_truth(condition):
    """Decorator that wraps a function to ensure it only executes if condition is True."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check truthiness of the passed argument (which should be a boolean or convertible)
            result = bool(condition)  # Convert input explicitly just in case
            return func(*args, **kwargs) if result else None
        return wrapper
    return decorator

# Example usage within main block to ensure it runs without external inputs
if __name__ == '__main__':
    
    @check_truth(True)      # Condition is True -> Function should run
    def add_numbers(a, b):
        """Adds two numbers."""
        return a + b
    
    @check_truth(False)     # Condition is False -> Function will not execute (returns None implicitly via wrapper logic or just skip execution in this specific design if we wanted to prevent side effects entirely. 
                           # However, the prompt says "only executes", so returning nothing on failure satisfies it.)
                            # Note: The standard pattern for 'if condition' decorators usually returns early without calling func().
    def multiply_numbers(a, b):
        """Multiplies two numbers."""
        return a * b
    
    print("Testing add_numbers (should execute):")
    result_add = add_numbers(5, 10)
    
    # To demonstrate the behavior where it doesn't run when condition is False, 
    # we can define a function that prints something. Since 'multiply' above returns None on failure,
    # let's redefine slightly to show side effect prevention clearly if needed, 
    # but sticking strictly to the prompt: "only executes". Returning early means execution didn't happen inside func().
    
    print("Testing multiply_numbers (condition False -> should not execute body):")
    result_mul = multiply_numbers(2, 3)
    
    print(f"Add Result: {result_add}") # Should be printed as function ran.
    print(f"Multiply Result: {result_mul}") # Will likely be None if we strictly return early without calling func().