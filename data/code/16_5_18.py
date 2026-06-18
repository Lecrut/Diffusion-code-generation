def positive_generator(iterable):
    """
    Generator function that yields True for every positive number 
    encountered in an input iterable.
    
    Args:
        iterable (iterable): An iterable of numbers to check.
        
    Yields:
        bool: True if the current item is a positive number, otherwise nothing yielded.
    """
    for item in iterable:
        if isinstance(item, (int, float)) and item > 0:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values containing mixed types including positives, negatives, zeros, strings, and booleans
    sample_data = [1, -5, 3.5, 0, "hello", False, 42, None]
    
    print("Testing positive number generator:")
    results = list(positive_generator(sample_data))
    print(f"Input: {sample_data}")
    print(f"Output (list of booleans for positives): {results}")