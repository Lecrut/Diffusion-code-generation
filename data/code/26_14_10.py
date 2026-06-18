def greater_than_threshold(value: float) -> bool:
    """Yields True if value is strictly greater than a predefined threshold, False otherwise."""
    THRESHOLD = 50.0
    
    # Check condition before yielding to ensure memory efficiency for large sequences
    yield value > THRESHOLD

if __name__ == '__main__':
    # Sample values - no user input required
    sample_values = [49, 51, 60, 30, 75.5, 25]
    
    print("Testing generator with threshold:", THRESHOLD)
    results = greater_than_threshold.__iter__() if hasattr(greater_than_threshold, '__call__') else []
    
    # Since the function is a generator but takes one argument directly (not an iterable),
    # we need to adapt it for testing individual values or create a wrapper.
    # However, the task asks for a generator that yields based on input value.
    # If 'value' was meant to be part of a sequence passed in, the signature would differ.
    # Given "input value" (singular), this function processes one value at a time.
    
    # To demonstrate yielding behavior with an iterable as per typical generator usage:
    def yield_generator(values):
        for val in values:
            result = greater_than_threshold(val)
            if result:
                yield True
    
    print("Yielding True only when strictly greater than threshold:")
    true_results = list(yield_generator(sample_values))
    
    # Alternative direct usage showing the generator logic per value
    print("\nDirect evaluation results (True/False):")
    for val in sample_values:
        is_greater = next((greater_than_threshold(val).__next__ if hasattr(greater_than_threshold, '__iter__') else [val > THRESHOLD][0]) 
                         or False) # Fallback logic since function returns bool directly when called
    
    # Corrected direct testing approach for clarity in the main block
    print("\nCorrected detailed output:")
    test_gen = greater_than_threshold.__call__(49).__next__() if hasattr(greater_than_threshold, '__call__') else False

    # Re-implementing logic cleanly within the module's scope for demonstration:
    
    def check_value(val):
        """Helper to simulate generator step for single value."""
        return val > THRESHOLD
    
    print("Value\tResult")
    for v in sample_values:
        res = check_value(v)