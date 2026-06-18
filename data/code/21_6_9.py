import sys

def reverse_range_generator(start: int, end: int):
    """
    Generator function that yields numbers from a given range in reverse order.
    
    Args:
        start (int): The lower bound of the range (inclusive).
        end (int): The upper bound of the range (inclusive).
        
    Yields:
        int: Numbers starting from 'end' down to 'start'.
        
    Example:
        >>> list(reverse_range_generator(1, 5))
        [5, 4, 3, 2, 1]
        
    Note: If start is greater than end, the function will yield no values.

    Memory Efficiency:
        This generator does not store all numbers in memory at once; 
        it yields one number at a time as requested by the caller.
    
    """
    if end < start:
        return
    
    for i in range(end, start - 1, -1):
        yield i

if __name__ == '__main__':
    # Sample usage with hard-coded values to demonstrate functionality without user input
    lower_bound = 50
    upper_bound = 37

    print("Generating numbers from", upper_bound, "down to", lower_bound)
    
    counter = 0
    for number in reverse_range_generator(lower_bound, upper_bound):
        if counter < 10:  # Print only the first few items to avoid excessive output
            print(number)
        else:
            break
        
        counter += 1
    
    total_count = sum(1 for _ in reverse_range_generator(lower_bound, upper_bound))
    print(f"Total numbers generated in range [{upper_bound}, {lower_bound}]:", total_count)