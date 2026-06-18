import os

# Hardcoded constant for validation
VALIDATION_THRESHOLD = 100

def validator(condition_func):
    """Decorator that checks if a condition is met before execution."""

    def wrapper(*args, **kwargs):
        # Get the first argument (if it exists) and pass it to the condition function
        arg_value = args[0] if args else None
        
        try:
            result = bool(condition_func(arg_value))
            
            if not result:
                raise ValueError(f"Condition failed. First argument ({arg_value}) is not greater than {VALIDATION_THRESHOLD}.")
                
            return condition_func(*args, **kwargs)
        
        except Exception as e:
            # If the original function raises an error that isn't from our check, propagate it
            if isinstance(e, ValueError):
                raise e
            
    wrapper.__name__ = f"wrapped_{condition_func.__name__}"
    
    return wrapper

@validator(lambda x: not (x <= VALIDATION_THRESHOLD))  # Condition: first arg must be > 100
def process_data(data_value):
    """Sample function to test the decorator."""
    print(f"Processing data with value {data_value}")
    result = f"{data_value} processed successfully."
    
    if isinstance(result, str) and len(result) < VALIDATION_THRESHOLD:
        return "Short string check failed internally too!"
        
    return {"status": "success", "value": data_value}

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    print("Test 1: Value less than threshold (should raise ValueError)")
    try:
        process_data(50)
    except ValueError as ve:
        print(f"Caught expected error: {ve}")

    print("\nTest 2: Value greater than or equal to threshold")
    result = process_data(101)
    if isinstance(result, dict):
        print("Result:", result)