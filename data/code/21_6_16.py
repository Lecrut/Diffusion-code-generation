def reverse_range_generator(start: int, end: int):
    """
    Generator function that yields numbers from a given range in reverse order.
    
    Args:
        start (int): The upper bound of the range.
        end (int): The lower bound of the range.
        
    Yields:
        int: Numbers starting from 'start' down to 'end'.
            
    Memory Efficiency:
        This generator yields numbers one at a time, avoiding storage 
        of the entire sequence in memory regardless of the range size.
    
    Raises:
        ValueError: If start is less than end or if they are not integers.
    """
    # Validate inputs to ensure logical range and integer types
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Both arguments must be integers.")
    if start < end:
        raise ValueError("Start value must be greater than or equal to end value for reverse iteration.")

    current = start
    
    while True:
        # Yield the current number and then decrement it. 
        # The loop condition (current >= end) ensures we stop after yielding 'end'.
        yield current
        
        if current <= end:
            break
            
        current -= 1

if __name__ == '__main__':
    # Hard-coded sample values for testing the generator without user input
    
    # Sample range from 5 to -2 (inclusive) in reverse order
    start_val = 5 
    end_val = -2 
    
    print(f"Generating numbers from {start_val} down to {end_val}:")
    
    # Iterate through and print each number yielded by the generator
    for num in reverse_range_generator(start_val, end_val):
        print(num)

    # Additional test case with a larger range to demonstrate memory efficiency capability conceptually
    large_start = 100 
    large_end = 95 
    
    print(f"\nGenerating numbers from {large_start} down to {large_end}:")
    
    for num in reverse_range_generator(large_start, large_end):
        # In a real-world scenario with very large ranges (e.g., millions), 
        # we would typically process the generator without printing every item 
        # directly here to avoid massive output. This demonstrates usage logic.
        pass 
    
    print("Generator completed.")