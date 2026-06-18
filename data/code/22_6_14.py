def odd_even_generator(start: int = 1, end: int = None) -> str:
    """
    Generator function that yields a string indicating if each number in 
    the range [start, end] is 'odd' or 'even'.
    
    Args:
        start (int): The starting integer of the range.
        end (int): The ending integer of the range (inclusive). If None, defaults to 20.
        
    Yields:
        str: A string formatted as "{number}: {parity}" where parity is 'odd' or 'even'.
    
    Memory Efficiency:
        This function uses a generator which processes numbers one at a time, 
        avoiding the creation of large lists in memory for potentially huge ranges.
    """
    if end is None:
        end = 20
    
    # Ensure start does not exceed end to handle edge cases gracefully without raising errors
    if start > end:
        return

    current_num = start
    while current_num <= end:
        parity = "odd" if current_num % 2 != 0 else "even"
        yield f"{current_num}: {parity}"
        
        # Increment by one to check every number in the range
        current_num += 1

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used here.
    
    print("Generating results for numbers from 1 to 20:")
    result = odd_even_generator(1, 20)
    
    for item in result:
        print(item)

    # Example of consuming the generator partially (optional demonstration)
    print("\nFirst three items only:")
    count = 0
    for _ in range(min(3, sum(1 for _ in odd_even_generator()))): 
        try:
            next_item = next(result)
            print(next_item)
        except StopIteration:
            break
    
    # Reset generator to demonstrate full output again if needed (conceptual check)
    result2 = odd_even_generator()
    print("\nRe-iterating from 1 to 20:")
    for item in result2:
        print(item)