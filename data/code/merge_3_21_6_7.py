import sys

def reverse_range_generator(start: int, end: int):
    """
    Generator function that yields numbers from 'start' down to 'end'.
    
    The generator is memory efficient as it produces one number at a time 
    without storing the entire range in a list. It assumes start >= end.
    
    Args:
        start (int): The upper bound of the range (inclusive).
        end (int): The lower bound of the range (inclusive).
        
    Yields:
        int: Numbers counting down from start to end.
    """
    if start < end:
        raise ValueError("Start value must be greater than or equal to end value.")
    
    while start >= end:
        yield start
        start -= 1

if __name__ == '__main__':
    # Sample usage with hard-coded values. 
    # This block runs without user input, command-line arguments, network access, or pre-existing files.
    lower_bound = 50
    upper_bound = 60
    
    print(f"Generating numbers from {upper_bound} down to {lower_bound}:")
    
    for num in reverse_range_generator(upper_bound, lower_bound):
        # Using sys.stdout directly ensures output is printed without any interactive prompts.
        sys.stdout.write(str(num) + '\n')