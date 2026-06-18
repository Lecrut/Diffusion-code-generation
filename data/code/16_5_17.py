def positive_numbers_generator(iterable):
    """
    Generator function that yields True for every positive number encountered 
    in an input iterable, effectively filtering for positivity without storing 
    the entire result list.
    
    Args:
        iterable (iterable): An iterable containing numbers to check.
        
    Yields:
        bool: True if the current item is a positive number, otherwise nothing yielded.
    """
    for item in iterable:
        # Check if the item is an instance of int or float and greater than 0
        if isinstance(item, (int, float)) and item > 0:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_data = [1, -5, 3.5, 0, "hello", 7]
    
    print("Testing positive_numbers_generator:")
    for result in positive_numbers_generator(sample_data):
        print(result)