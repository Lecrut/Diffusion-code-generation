def positive_generator(iterable):
    """
    Generator function that yields True for every positive number encountered in an input iterable.
    
    Args:
        iterable (iterable): An iterable containing numbers to check.
        
    Yields:
        bool: True if the current element is a positive number, otherwise does not yield anything.
    """
    for item in iterable:
        # Check if the item is an instance of int or float and greater than 0
        if isinstance(item, (int, float)) and item > 0:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values including positive numbers, negatives, zero, strings, and floats
    sample_data = [1, -5, 3.5, "hello", 0, 7, False, 2.9]
    
    print("Testing positive generator:")
    results = list(positive_generator(sample_data))
    print(f"Input: {sample_data}")
    print(f"Output (list of booleans): {results}")