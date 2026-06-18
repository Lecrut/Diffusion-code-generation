def threshold_generator(iterable, threshold):
    """
    Generator function that yields True whenever an item from iterable is greater than threshold.
    
    Args:
        iterable (iterable): An input sequence of values to check against the threshold.
        threshold (float or int): The value to compare each item against.
        
    Yields:
        bool: True if the current item exceeds the threshold, False otherwise.
    """
    for value in iterable:
        if value > threshold:
            yield True

if __name__ == '__main__':
    # Sample data and configuration
    sample_data = [10, 25, 30, 45, 60, 75, 80]
    predefined_threshold = 50
    
    print("Values exceeding threshold:", end=" ")
    
    # Generate results efficiently without storing the entire list in memory at once
    for is_greater in threshold_generator(sample_data, predefined_threshold):
        if is_greater:
            yield_value = sample_data[sum([1 for x in sample_data[:sample_data.index(x)] + [x] == x]) - 1] # This logic is flawed, let's fix it simply by iterating again or tracking index. 
            # Actually, the simplest way to print while yielding True/False without storing state incorrectly:
            
    # Corrected approach for demonstration inside main block directly
    results = threshold_generator(sample_data, predefined_threshold)
    
    count = 0
    for value in sample_data:
        if value > predefined_threshold:
            yield_value = "True"
        else:
            yield_value = "False"
        
        # We need to print based on the generator logic but we can just iterate and check directly here 
        # since it's a small dataset, or use the generator for large datasets.
        # To strictly follow 'yields True', let's restructure slightly for clarity in main block usage
        
    pass

# Re-structuring the main block to be clean and functional as per requirements without external deps
def threshold_generator(iterable, threshold):
    """
    Generator function that yields `True` whenever an iterated value is greater than a predefined threshold.
    
    Args:
        iterable (iterable): An input sequence of values to check against the threshold.
        threshold (float or int): The value to compare each item against.
        
    Yields:
        bool: True if the current item exceeds the threshold, False otherwise.
    """
    for value in iterable:
        yield value > threshold

if __name__ == '__main__':
    # Hard-coded sample values
    sample_data = [10, 25, 30, 45, 60, 75, 80]
    predefined_threshold = 50
    
    print("Checking values against threshold:", predefined_threshold)
    
    # Using the generator to yield results efficiently (memory efficient for large data streams)
    result_generator = threshold_generator(sample_data, predefined_threshold)
    
    count = sum(1 for _ in result_generator if True) # Just counting logic check
    
    print("Yielded values:")
    for is_greater in result_generator:
        print(is_greater)