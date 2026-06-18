def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes if 'condition' is True.
    
    Args:
        condition (Any): The value to evaluate as truthy or falsy.
        
    Returns:
        Decorator function
    
    Example usage:
        @check_truth(True)
        def my_function(): pass
        
        # If the decorator was check_truth(False), this would not run
    """
    def decorator(func):
        if condition is True:
            return func
        else:
            def wrapper(*args, **kwargs):
                print(f"Function {func.__name__} skipped because condition ({condition}) is falsy.")
                return None
            
            wrapper.__name__ = f"{func.__name__}_skipped"
            return wrapper
        
    return decorator

def sample_function(value):
    """An example function to be wrapped."""
    print(f"Running {sample_function.__name__} with value: {value}")
    result = value * 2
    print(f"Result: {result}")
    return result

if __name__ == '__main__':
    # Example where the decorator runs because condition is True
    @check_truth(True)
    def run_when_true():
        print("This block executed successfully.")
    
    # Define a function to be skipped due to False condition in another context (demonstrating logic)
    # Note: We are demonstrating usage within this module's main block.
    
    # Test case 1: Condition is True, function should run
    print("--- Testing with Truthy Condition ---")
    @check_truth(True)
    def test_function_1():
        return "Success"
    
    result_test_1 = test_function_1()
    if not isinstance(result_test_1, str):
        raise Exception("Expected string from function wrapped in check_truth(True)")

    # Test case 2: Simulating a scenario where the decorator prevents execution.
    # Since decorators are applied at definition time with static values here, 
    # we will demonstrate by defining a wrapper manually to show what happens when condition is False.
    
    def dummy_function():
        print("This should not run if wrapped incorrectly.")

    # To simulate check_truth(False) behavior dynamically for demonstration:
    @check_truth(False)  # This effectively disables the wrapping logic's execution path for this function? 
                        # No, because decorators bind at definition time. The 'condition' is fixed when '@decorator(arg)' is parsed.
                        # However, we can show how it behaves by defining another one with False explicitly if needed in a different scope or just relying on the True case above being sufficient for execution proof.
    
    # Let's create a function that would be skipped based on our decorator logic definition.
    @check_truth(False) 
    def test_function_2():
        print("This should not run.")

    result_test_2 = test_function_2()  # This will execute the wrapper which prints "skipped" message and returns None
    
    if result_test_1 is None:
        raise Exception("Test function with True condition failed")
    
    if isinstance(result_test_2, str): 
        raise Exception(f"Expected skipped behavior for False condition. Got {result_test_2}")

    print("--- All tests passed ---")