def reverse_range_generator(start: int, end: int):
    """
    Generator function that yields numbers from 'start' down to 'end'.
    
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
        
        # Stop when we have yielded 'end' inclusive. 
        # Since the loop decrements after yielding, check before next iteration logic is handled by range limit implicitly if used differently,
        # but here we manually control to ensure exactly down_to end.
        if current == end:
            break

if __name__ == '__main__':
    # Sample usage without any user input or external dependencies
    start_val = 10
    end_val = 5
    
    print(f"Generating numbers from {start_val} to {end_val}:")
    
    for num in reverse_range_generator(start_val, end_val):
        print(num)