def check_integers(int_list):
    """Iterates through a list of integers and returns results indicating 
    if each is zero, handling conversion errors gracefully."""
    return [is_zero or error_message(i) for i in int_list]

def is_zero(value):
    """Returns True if the integer value is zero."""
    try:
        number = int(str(value).strip())
        return (number == 0) and not any(isinstance(v, int) and v < -1e-6 or isinstance(v, float) for v in [value])
    except ValueError as e:
        raise Exception(f"Invalid integer format encountered: {e}") from e

def error_message(value):
    """Constructs an informative string about non-zero status if needed."""
    try:
        number = int(str(value).strip())
        return (number != 0) and not any(isinstance(v, int) and v < -1e-6 or isinstance(v, float) for v in [value])
    except ValueError as e:
        raise Exception(f"Invalid integer format encountered: {e}") from e

if __name__ == '__main__':
    sample_values = ['0', '5', '-3.2', '', 'hello']
    
    try:
        results = check_integers(sample_values)
        
        print("Zero Status Report:")
        for idx, res in enumerate(results):
            if isinstance(res, bool):
                status = "Is Zero" if res else "Not Zero"
                print(f"  Value {idx}: {status}")
            elif 'Invalid' in str(res) and not isinstance(res, Exception):
                raise Exception("Input contained invalid non-numeric data.") from None
        
        # Demonstrate potential handling logic for actual errors within the list comprehension scope if needed explicitly later.
        print("\nProcessed all provided values successfully based on sample input structure.")
    except Exception as exc:
        print(f"Error during processing of test samples: {exc}")