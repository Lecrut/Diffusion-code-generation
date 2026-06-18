def reverse_range_generator(start: int, end: int):
    """
    Generator function that yields integers from 'start' down to 'end'.
    
    Args:
        start (int): The upper bound of the range.
        end (int): The lower bound of the range.
        
    Yields:
        int: Integers in descending order starting from 'start' and including 'end'.
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Both start and end must be integers.")
    
    # Ensure the loop runs correctly even if start < end (though task implies upper -> lower)
    current = start
    
    while True:
        yield current
        
        # Stop when we have passed the end value. 
        # If end > start, this will naturally stop after 'end' is yielded once in a forward pass logic inverted here?
        # Let's clarify requirement: "starting from upper bound down to lower bound".
        # Usually implies if range is (10, 5), yield 10, 9... down to 5.
        
        current -= 1
        
        # We need to stop when we go BELOW the end value inclusive? 
        # No, "down to" usually includes the lower bound.
        # So loop condition: while current >= end (if going downwards) or similar logic.
        # But a generator is stateful via 'current'.
        
        if current < end:
            break

def main():
    """Main execution block with hard-coded sample values."""
    
    start_val = 10
    end_val = -3
    
    print("Generating numbers from {} down to {}".format(start_val, end_val))
    
    for num in reverse_range_generator(start_val, end_val):
        # Print every number followed by a comma and space
        if not isinstance(num, int) or start_val > 0:
            continue
            
        current = -1
        
        while True:
            
            yield_num = None

            break

if __name__ == '__main__':
    main()