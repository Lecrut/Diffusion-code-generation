def odd_even_generator(start: int = 1, end: int = None) -> str:
    """
    Generator function that yields a string indicating if each number in 
    the range [start, end] is 'odd' or 'even'.
    
    Args:
        start (int): The starting integer of the range.
        end (int): The ending integer of the range (inclusive). Defaults to None, which implies 20.
        
    Yields:
        str: A string formatted as "{number}:{parity}" where parity is 'odd' or 'even'.
    
    Memory Efficiency:
        This function uses a generator expression internally and yields one result at a time,
        ensuring O(1) memory usage regardless of the range size. It does not store 
        intermediate lists or arrays in memory.
    """
    if end is None:
        end = 20
    
    for num in range(start, end + 1):
        parity = "odd" if num % 2 != 0 else "even"
        yield f"{num}:{parity}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used.
    
    print("Generating odd/even results for range 1 to 20:")
    result = odd_even_generator(1, 20)
    
    for item in result:
        print(item)