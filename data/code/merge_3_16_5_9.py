def is_positive_generator(iterable):
    """
    Generator function that yields True for every positive number 
    encountered in an input iterable, without storing intermediate results.
    
    Args:
        iterable (iterable): An input sequence of numbers or mixed types
        
    Yields:
        bool: Boolean indicating if the current value is a positive integer
               Only True values are yielded; False/None values are skipped internally but 
               we still return True only for valid positive integers. For non-integers,
               this implementation yields nothing to strictly adhere to "filtering".
    """
    # We need to yield True ONLY when the input is a POSITIVE INTEGER.
    # If it's not an int (e.g., float like 5.0), we skip yielding anything 
    # or could yield False? The task says 'yields True for every positive number'.
    # Usually "number" implies numeric types, but strictly speaking integers are the standard 
    # interpretation in discrete contexts unless specified as inclusive of floats.
    # However, to be safe and robust: if it's a valid int > 0 -> yield True.
    
    try:
        for item in iterable:
            # Check if item is an integer (not float) and positive
            if isinstance(item, int):
                if item > 0:
                    yield True
            else:
                # If it's not an int (e.g., string '5', float 5.7), do nothing 
                # to strictly filter for "positive numbers" as integers usually intended in such tasks.
                pass
                
    except TypeError:
        # Handle cases where the iterable might contain non-iterable elements at runtime
        return

if __name__ == '__main__':
    # Hard-coded sample values that do not require user input, network access, or files
    test_data = [10, 2, -5, 3.7, '4', True, None] 
    
    for num in is_positive_generator(test_data):
        print(num)