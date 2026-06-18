def odd_even_generator(start=1, end=None):
    """
    A generator function that yields results of odd/even checks 
    for every number in a given range [start, end).
    
    Parameters:
        start (int): The starting integer.
        end (int or None): The ending integer. If None, defaults to 100.
    
    Yields:
        tuple: A tuple containing the current number and its parity ('odd' or 'even').
    
    Memory Efficiency:
        This function uses a generator which yields one value at a time 
        rather than storing all results in memory (e.g., as a list).
    """
    if end is None:
        end = 100
    
    for number in range(start, end):
        parity = 'odd' if number % 2 != 0 else 'even'
        yield number, parity

if __name__ == '__main__':
    # Sample execution without user input or command-line arguments
    sample_range_start = 1
    sample_range_end = 20
    
    for num_info in odd_even_generator(sample_range_start, sample_range_end):
        print(num_info)