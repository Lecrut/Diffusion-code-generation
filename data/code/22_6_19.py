def odd_even_generator(start: int = 1, end: int = None) -> bool:
    """
    Generator function that yields True if a number is even, False otherwise.
    
    Args:
        start (int): The starting number of the range (inclusive). Default is 1.
        end (int): The ending number of the range (exclusive). If None, defaults to 20.
        
    Yields:
        bool: True for even numbers, False for odd numbers.
    
    Memory Efficiency Note: This function uses a generator which processes 
    one number at a time and yields immediately upon completion, avoiding 
    the creation of large lists in memory.
    """
    if end is None:
        end = 20
    
    current_num = start
    while current_num < end:
        yield (current_num % 2 == 0)
        current_num += 1

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    range_start = 1
    range_end = 20
    
    print("Odd/Even Check Results:")