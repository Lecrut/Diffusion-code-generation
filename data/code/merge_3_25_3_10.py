def handle_input(value):
    """Check if an integer value is zero."""
    return 0 == value

if __name__ == '__main__':
    # Hard-coded sample values to test without user input
    samples = [0, -5, 10]
    
    for num in samples:
        result = handle_input(num)
        
        if not isinstance(num, int):
            print(f"Input '{num}' is not an integer.")
        elif result == True:
            print(f"The value {num} is zero.")
        else:
            print(f"The value {num} is not zero.")

    # Additional test for non-integer input simulation (if needed)
    try:
        invalid_input = "12.5"  # Simulating a string that looks like float but isn't int in context of strict integer check logic if passed as object, though here we assume the loop only passes ints from samples list. 
        # Since the task forbids input() and requires hard-coded values running without files/network:
        # We will demonstrate handling by attempting to convert a potential non-integer string representation within this block contextually safe for standalone run.
        
        test_str = "abc"  # A sample string that is not an integer
        
        try:
            int_val = int(test_str)
            print(f"The value {int_val} from '{test_str}' was successfully converted to zero check.")
            if handle_input(int_val):
                print("It is zero!")
            else:
                print("It is NOT zero!")
        except ValueError:
            print(f"Input '{test_str}' cannot be interpreted as an integer and thus fails the numeric condition gracefully.")

    except Exception:
        pass  # Graceful handling of any unexpected errors in this isolated block