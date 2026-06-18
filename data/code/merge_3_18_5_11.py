def strictly_increasing_generator(sequence):
    """
    Generator that yields True if the current value is strictly greater 
    than the previous value in the input sequence, otherwise False (or skips).
    
    Note: The problem statement says "yields True only when...", which implies 
    yielding a boolean flag for each comparison. However, standard practice for 
    such checks often involves skipping non-increasing steps or returning 0/1.
    Given the phrasing "yields True", we will yield True on increase and False otherwise,
    starting from index 1 to compare with previous element.

    Args:
        sequence (iterable): An iterable of comparable values.
    
    Yields:
        bool: True if current > previous, else False.
    """
    try:
        prev = next(sequence)
    except StopIteration:
        return
    
    for curr in sequence:
        # Compare strictly greater than the previous value yielded so far
        if curr > prev:
            yield True
        else:
            yield False
        
        prev = curr

if __name__ == '__main':
    # Hard-coded sample values to test the generator without user input or files.
    data = [1, 5, 3, 8, 2, 9]

    print("Input sequence:", data)
    
    results = list(strictly_increasing_generator(data))
    print("Comparison results (True if increasing):", results)

if __name__ == '__main__':
    pass
