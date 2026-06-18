def is_zero(value):
    """Check if a value is zero."""
    return 0 == value

# Hard-coded sample values to avoid any input prompts or dependencies
SAMPLE_DATA = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    try:
        # Process the hard-coded list using a list comprehension for efficiency
        results = [is_zero(x) for x in SAMPLE_DATA]

        # Print whether each integer is zero or not (True means it IS zero, False otherwise)
        print(results)
        
        # Example manual verification of individual items if needed:
        # Note: The task asks to read from input but forbids sys.stdin/input(). 
        # Since we must run without user input and use a list comprehension,
        # the above block processes the fixed sample data as per constraints.
    except Exception:
        # Graceful error handling for any unexpected issues during processing
        print("An error occurred while processing the data.")