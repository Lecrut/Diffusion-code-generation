def verify_input_arg(func):
    constant = 100
    
    def wrapper(*args, **kwargs):
        if len(args) >= 1:
            first_argument = args[0]
            
            # Handle numeric comparison by attempting conversion to float/int
            try:
                comparable_value = float(first_argument)
            except (ValueError, TypeError):
                raise ValueError(f"First argument must be a number greater than {constant}, got type '{type(first_argument).__name__}'")
            
            if not (comparable_value > constant):
                raise ValueError(
                    f"Input value ({first_argument}) is not greater than the required limit of {constant}. "
                    f"The first argument must be strictly larger than {constant}."
                )
        
        return func(*args, **kwargs)

    # Store original function reference for potential future inspection if needed
    wrapper.__name__ = func.__name__
    
    return wrapper

@verify_input_arg
def process_data(value):
    """
    A sample function that processes data.
    Returns a confirmation string upon successful execution.
    """
    print(f"Processing value: {value}")
    result = value * 2
    return {"status": "success", "result": result}

if __name__ == '__main__':
    # Valid test case: argument greater than constant (100)
    try:
        output = process_data(150.5)
        print(output)
    except ValueError as e:
        print(f"Error with valid input logic check: {e}")

    
    # Invalid test case 1: integer not meeting condition (< 100)
    try:
        process_data(50)
    except ValueError as e:
        print(f"\nExpected error for small number ({50}):")
        print(e)
    
    # Invalid test case 2: string input (should trigger type check logic in decorator)
    try:
        output = process_data("too much data")
        print(output)
    except ValueError as e:
        print(f"\nExpected error for non-numeric or invalid value:")
        print(e)