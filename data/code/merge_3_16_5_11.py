def positive_numbers_generator(iterable):
    """
    Generator function that yields True for every positive number encountered 
    in an input iterable, without storing the entire result list.
    
    Args:
        iterable (iterable): An input sequence of numbers to process.
        
    Yields:
        bool: True if the current element is a positive number, otherwise not yielded.
    """
    for item in iterable:
        # Check if the item is an instance of int or float and strictly greater than zero
        if isinstance(item, (int, float)) and item > 0:
            yield True

if __name__ == '__main__':
    sample_data = [1, -2, 3.5, 0, 4, "negative", 7]
    
    # Generate results without storing them in a list (memory efficient)
    result_generator = positive_numbers_generator(sample_data)
    
    print("Positive numbers detected:")
    for is_positive in result_generator:
        if is_positive:
            # We iterate again or store temporarily just to show which were found, 
            # but the generator itself only yielded True. To demonstrate values,
            # we can re-iterate with a filter logic inside since it's small data.
            pass
    
    # Re-implementing display loop directly without external storage for clarity in this context:
    count = 0
    for item in sample_data:
        if isinstance(item, (int, float)) and item > 0:
            print(f"Found positive number: {item}")
            yield_result = True # Simulate the generator output logic here directly 
                                 # since we are demonstrating execution. In a real usage, 
                                 # you would just iterate over 'positive_numbers_generator(sample_data)'.