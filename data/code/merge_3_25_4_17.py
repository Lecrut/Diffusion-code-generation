def is_zero_generator(iterable):
    """
    Generator that yields True if any number in an iterable list is zero, 
    and False otherwise after checking all elements.

    Memory efficient: processes items one by one without loading the entire list into memory at once.
    
    Args:
        iterable (iterable): An iterable of numbers to check for zeros.
        
    Yields:
        bool: True if a zero is found, False otherwise after iteration completes.
             Note: This generator yields exactly one value based on whether any element was zero.
    """
    has_zero = False
    
    # Process items one by one without loading the whole list into memory
    for item in iterable:
        try:
            if item == 0 or (isinstance(item, float) and item == 0):
                yield True
                return
        
        except TypeError:
            continue
            
    # If loop completes without finding zero
    yield False

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test case 1: List containing a zero
    sample_1 = [5, 0, -3]
    
    # Test case 2: List not containing any zeros
    sample_2 = [1, 2, 3]
    
    # Test case 3: Empty list
    sample_3 = []
    
    # Test case 4: Float zero
    sample_4 = [0.5, -0.1, 0.0]
    
    print("Testing is_zero_generator:")
    
    for test_name, test_data in [("With Zero", sample_1), ("Without Zero", sample_2), 
                                 ("Empty List", sample_3), ("Float Zero", sample_4)]:
        result = list(is_zero_generator(test_data))
        print(f"{test_name}: {result}")