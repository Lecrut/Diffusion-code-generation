def verify_input(condition_value=100):
    """Decorator factory that verifies if the first argument is greater than a constant."""
    
    def decorator(func):
        # Use functools.wraps to preserve original function metadata
        import functools
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Check if at least one positional argument exists and its value meets the condition
            if args:
                first_arg = args[0]
                
                try:
                    numeric_value = float(first_arg)
                except (TypeError, ValueError):
                    raise TypeError(f"First argument must be convertible to a number. Got {type(first_arg)}") from None
                
                if not (numeric_value > condition_value):
                    raise ValueError(
                        f"The first argument ({first_arg}) is not greater than the constant "
                        f"{condition_value}. Please provide a value larger than {condition_value}."
                    )
            
            # If no arguments or all pass validation, execute original function
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

def process_data(value):
    """Sample function to demonstrate the decorator."""
    print(f"Processing data with value: {value}")
    
# Apply decorators
@verify_input()  # Default constant is 100
def run_task_1():
    result = process_data(25) 
    return result

if __name__ == '__main__':
    try:
        output1 = run_task_1()
        print(f"Task 1 Result: {output1}")
        
        # Attempt with invalid value (less than or equal to constant)
        @verify_input(50) 
        def fail_test():
            return process_data(49)
        
        try:
            result = fail_test()
        except ValueError as e:
            print(f"Caught expected error for low value: {e}")
            
    except Exception as e:
        if "not greater than the constant" in str(e):
            print("Validation logic working correctly.")
        else:
            raise