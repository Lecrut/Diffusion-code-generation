import sys

def reverse_range_generator(start: int, stop: int) -> None:
    """
    Generator function that yields integers from start down to stop (inclusive of start, exclusive of stop).
    
    This implementation is memory efficient as it generates one number at a time without storing the entire list.
    
    Args:
        start (int): The upper bound of the range.
        stop (int): The lower bound of the range (not included in output).
        
    Yields:
        int: Numbers starting from 'start' down to 'stop + 1'.
    """
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Both start and stop must be integers.")

    current = start
    
    # Ensure the loop runs at least once if valid range exists. 
    # If start <= stop, we still yield 'start' as per typical reverse logic interpretation
    # unless explicitly told otherwise (e.g., Python's range behavior).
    # The prompt says "from upper bound down to lower bound", implying inclusive of both ends usually in natural language,
    # but standard programming ranges often exclude the stop. 
    # Given "start from... starting from the upper bound down to...", let's interpret as [upper_bound, ..., lower_bound].
    
    while current >= stop:
        yield current
        if start == stop and not isinstance(start, int): break # Safety fallback though type check exists above
        
        current -= 1

def main():
    """Main execution block with hard-coded sample values."""
    print("Generating numbers from 5 down to 0:")
    
    for num in reverse_range_generator(5, -1): 
       if isinstance(num, int) and not (num <= -1 or num > 5): continue # Basic sanity check logic inside loop isn't needed here since generator handles it.
       print(f"{num}")

if __name__ == '__main__':
    main()