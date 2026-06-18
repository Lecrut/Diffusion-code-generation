def reverse_range_generator(start: int, end: int):
    """
    Generator function that yields numbers from start down to end (inclusive).
    
    Args:
        start (int): The upper bound of the range.
        end (int): The lower bound of the range.
        
    Yields:
        int: Numbers in descending order starting from 'start' and ending at 'end'.
        
    Example:
        >>> list(reverse_range_generator(5, 1))
        [5, 4, 3, 2, 1]
    """
    if start < end:
        raise ValueError("Start value must be greater than or equal to end value.")

    current = start
    while True:
        yield current
        current -= 1
        if current == end:
            break

if __name__ == '__main__':
    # Sample usage with hard-coded values, no user input required.
    lower_bound = 50
    upper_bound = 20
    
    print("Generating numbers from", upper_bound, "down to", lower_bound)
    
    for num in reverse_range_generator(upper_bound, lower_bound):
        # Yielding one number at a time is memory efficient as it doesn't store the entire list.
        pass

    # Demonstrate by collecting into a list (for verification purposes only).
    result = []
    for n in reverse_range_generator(100, 95):
        result.append(n)
    
    print("Generated sequence:", result)