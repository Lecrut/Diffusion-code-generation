def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes 
    if the provided condition is True.
    
    Args:
        condition (bool or any truthy value): The condition to evaluate before execution.
        
    Returns:
        Decorated function wrapped in logic that checks 'condition' first.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not bool(condition):
                print(f"Execution skipped because condition is falsy: {bool(condition)}")
                return None
            
            result = func(*args, **kwargs)
            
            # If the function returns a value that evaluates to False (like 0 or empty list), 
            # we still consider it executed successfully unless explicitly told otherwise.
            if not bool(result):
                print(f"Function returned falsy value: {result}")
                
            return result
        
        return wrapper
    
    return decorator

if __name__ == '__main__':
    @check_truth(True)  # Condition is True, function should execute
    def greet(name):
        """Greet a person."""
        print(f"Hello, {name}!")
        return name.upper()

    @check_truth(False)  # Condition is False, function should NOT execute
    def secret_message(msg):
        """Prints a secret message (should not run)."""
        print("This is the secret code: X7D9")
        return "X7D9"

    @check_truth(10 > 5)  # Condition evaluates to True, function should execute
    def calculate(x):
        """Calculate double of x."""
        result = x * 2
        print(f"Doubled value: {result}")
        return result

    # Test cases with hard-coded values
    greet("Alice")          # Should run and output "Hello, Alice!" then "ALICE"
    
    secret_message("Keep it safe!")  # Should NOT run
    
    calculate(20)           # Should run and print "Doubled value: 40", return 40

    # Demonstrate falsy result handling (optional logic check based on requirement interpretation)
    @check_truth(True)
    def get_zero():
        """Returns a falsy number."""
        return 0
    
    zero_result = get_zero()
    
    print(f"Final results: Alice's greeting executed, Secret skipped, Zero returned.")