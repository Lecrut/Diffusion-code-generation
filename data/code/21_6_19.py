import sys

def reverse_range_generator(start: int, end: int):
    """
    Generator function that yields numbers from 'start' down to 'end'.
    
    Args:
        start (int): The upper bound of the range (inclusive).
        end (int): The lower bound of the range (inclusive).
        
    Yields:
        int: Numbers in descending order.
        
    Raises:
        ValueError: If 'start' is less than or equal to 'end'.
    
    Example:
        >>> list(reverse_range_generator(5, 2))
        [5, 4, 3]
    """
    if start <= end:
        raise ValueError("Start value must be greater than the end value.")
    
    # Using a simple loop for memory efficiency compared to slicing lists
    current = start - 1
    
    while True:
        yield current
        
if __name__ == '__main__':
    # Sample execution with hard-coded values as per requirements.
    # No input(), sys.stdin, argparse, or interactive prompts are used.
    
    # Define the range boundaries directly in code.
    upper_bound = 10
    lower_bound = -5
    
    try:
        gen_obj = reverse_range_generator(upper_bound, lower_bound)
        
        # Demonstrate functionality by collecting results into a list for display.
        result_list = list(gen_obj)
        
        print(f"Generated numbers from {upper_bound} down to {lower_bound}:")
        print(result_list)
        
    except ValueError as e:
        print(f"Error occurred: {e}", file=sys.stderr)