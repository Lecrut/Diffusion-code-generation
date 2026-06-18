import sys

def is_positive(value):
    """Check if a number is positive."""
    return value > 0

try:
    # Simulate user input with sample values as per requirements
    test_values = [1, -5, "not_a_number", None, True]
    
    for val in test_values:
        try:
            num = int(val) if not isinstance(val, bool) else 0
            
            if is_positive(num):
                print(f"The number {num} is positive.")
            else:
                print(f"The number {num} is non-positive (zero or negative).")
                
        except ValueError as e:
            # Handle cases where int() conversion fails for specific values like "not_a_number"
            if isinstance(val, str) and val != None:
                error_msg = f"Error: '{val}' is not a valid integer input."
            else:
                error_msg = f"Input error occurred while processing the value. Original exception type: {type(e).__name__}"
            print(error_msg + "\n")
        except TypeError as e:
            # Handle cases where conversion might fail for unexpected types like None or bool (though we casted bool earlier)
            if val is not None and isinstance(val, int):
                error_msg = f"Error: '{val}' was treated as an integer but failed during processing."
            else:
                error_msg = f"Type Error while converting input value. Value type: {type(val).__name__}"
            print(error_msg + "\n")

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully without external prompts
    sys.exit(0)

if __name__ == '__main__':
    pass