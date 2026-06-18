def reverse_range_generator(lower_bound: int, upper_bound: int):
    """
    Generator function that yields numbers from lower_bound to upper_bound in reverse order.
    
    Args:
        lower_bound (int): The starting lower limit of the range.
        upper_bound (int): The ending upper limit of the range.
        
    Yields:
        int: Numbers counting down from upper_bound to lower_bound inclusive.
        
    This function is memory efficient as it yields one number at a time 
    rather than storing the entire list in memory.
    
    Raises:
        ValueError: If upper_bound is less than lower_bound.
    """
    if upper_bound < lower_bound:
        raise ValueError("upper_bound must be greater than or equal to lower_bound.")
    
    for number in range(upper_bound, lower_bound - 1, -1):
        yield number

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, network access, or file I/O is used.
    
    start = 0
    end = 5
    
    print(f"Generating numbers from {start} down to {end}:")
    
    for num in reverse_range_generator(start, end):
        print(num)