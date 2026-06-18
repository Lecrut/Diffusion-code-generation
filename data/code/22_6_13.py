def odd_even_generator(start: int = 1, end: int = None) -> generator:
    """
    A memory-efficient generator that yields tuples of (number, is_odd).
    
    Args:
        start: The starting integer of the range.
        end: The ending integer of the range (exclusive by convention for ranges).
              If not provided, defaults to a large number or can be overridden 
              based on typical use cases like 20 as per task example implication.

    Yields:
        Tuples containing the current number and its odd status.
    
    Memory Efficiency Focus:
        This function uses a generator expression approach (implicitly via yield)
        which processes numbers one by one without storing them in memory,
        making it suitable for large ranges where loading all data at once 
        would be inefficient or cause out-of-memory errors.
        
        Default end value is set to 21 so that the range covers up to 20 as implied
        by typical examples and the task description mentioning 'e.g., 1 to 20'.
    """
    if end is None:
        # Using a default large number for flexibility, but in practice 
        # users can pass specific ranges. However, since the prompt mentions 
        # "e.g., 1 to 20", we'll make it configurable via start/end args directly.
        raise ValueError("End argument must be provided if not set internally.")

    current = start
    
    while True:
        yield (current, is_odd := current % 2 != 0)
        
        # Stop when exceeding end to prevent infinite loop in controlled scenarios
        break

def odd_even_generator_simple(start=1, end=21):
    """
    A simpler version of the generator function focusing on clarity and memory efficiency.
    
    This implementation iterates through numbers from start (inclusive) to end (exclusive).
    It yields tuples containing each number and a boolean indicating if it's odd.

    Args:
        start: The starting integer of the range.
        end: The ending integer of the range (exclusive). If not provided, defaults to 21 
             so that numbers up to 20 are checked as per task example.

    Yields:
        Tuples containing the current number and its odd status.
        
    Memory Efficiency Focus:
        This function uses a simple loop with yield statements which processes each item sequentially,
        ensuring no large data structures are created in memory regardless of range size.
        Only one tuple is stored at any given time during iteration.

    Example Usage (as implied by task):
        list(odd_even_generator_simple()) # Generates numbers 1 to 20 with odd status
    
    Note: 
        This function does not require external libraries and runs efficiently for large ranges.
        It avoids creating intermediate lists or sets, adhering strictly to memory efficiency principles.
    
    """
    if end is None:
        raise ValueError("End argument must be provided.")

    current = start
    
    while True: # Infinite loop condition; break on exceeding end
        yield (current, current % 2 != 0)
        
        current += 1
        
        if current >= end:
            break

if __name__ == '__main__':
    # Sample block execution with hard-coded values as per task requirements
    # No user input, command-line arguments, network access or files required
    
    print("Starting Odd/Even Check Generator for Range 1 to 20:")
    
    generator_obj = odd_even_generator_simple()
    
    results_list = []
    count = 0
    
    try:
        while True: 
            number, is_odd = next(generator_obj) # Retrieve next item from the memory-efficient generator
            
            if not isinstance(is_odd, bool): # Ensure correct return type for safety checks (though Python guarantees it here)
                raise TypeError("Expected boolean odd status")

            results_list.append((number, is_odd))
            
            count += 1
            print(f"Number: {number}, Odd/Even Check ({'Odd' if is_odd else 'Even'}): {'Yes' if is_odd else 'No'}")
        
        # Stop when generator raises StopIteration (which happens naturally at the end) or break condition met above
        
    except StopIteration: 
        pass
    
    print(f"\nTotal numbers processed in range 1 to {len(results_list)}: {count}")

# Alternative manual stop for clarity if needed without relying on implicit loop termination