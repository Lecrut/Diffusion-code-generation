def check_truth(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                print(f"Condition {condition} is False; function not executed.")
                return None
        return wrapper
    return decorator

@check_truth(True)
def safe_function():
    """A function that runs only when the condition is True."""
    result = "Function executed successfully."
    print(result)
    return result

if __name__ == '__main__':
    # Hard-coded sample values for testing
    test_condition_true = True
    
    @check_truth(test_condition_true)
    def another_safe_func():
        """Another function wrapped with the decorator."""
        value = 42
        print(f"Value is {value}")
    
    # Test case where condition is True (should execute)
    if test_condition_true:
        safe_function()
        
    # Test case where we pass a different condition that might be False locally 
    # but here we explicitly set it to True again for this run.
    local_test = True
    
    @check_truth(local_test)
    def third_safe_func():
        """Function testing with another variable."""
        msg = "This message is printed."
        print(msg)
    
    if local_test:
        another_safe_func()