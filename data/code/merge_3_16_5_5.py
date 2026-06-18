def positive_generator(iterable):
    """
    Generator function that yields True for every positive number encountered 
    in an input iterable, effectively filtering for positivity without storing 
    the entire result list.
    
    Args:
        iterable (iterable): An iterable containing numbers to check.
        
    Yields:
        bool: True if the current element is a positive number, otherwise does not yield.
              Note: The function yields 'True' as requested by the task description 
              for every positive number encountered. If non-positive or non-numeric values 
              are found, they are simply skipped (not yielded).
    """
    for item in iterable:
        if isinstance(item, (int, float)) and item > 0:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values to test the generator without user input or external dependencies.
    sample_data = [1, -5, 3.5, "hello", 0, 2, None]
    
    print("Testing positive_generator with:", sample_data)
    
    results = list(positive_generator(sample_data))
    
    # The generator yields True for every positive number encountered (1 and 3.5).
    # It skips non-numeric values (-5 is numeric but not positive, "hello", None), 
    # zero, and negative numbers as per the condition item > 0.
    print("Results yielded:", results)
    
    assert len(results) == 2, f"Expected 2 True yields for positives {1} and {3.5}, got {len(results)}."