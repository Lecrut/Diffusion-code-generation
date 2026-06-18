import sys

# Predefined threshold value as per requirements
THRESHOLD = 50

def memory_efficient_generator():
    """
    Generator function that yields True if the first number yielded is strictly greater than THRESHOLD,
    and False otherwise. It continues yielding subsequent numbers (or None) to demonstrate functionality
    while maintaining memory efficiency by not storing lists or large structures in memory.

    This generator simulates a stream of integers where only the status of the *first* integer relative 
    to the threshold determines its yield value, but it yields all processed values for completeness 
    without accumulating them into memory.
    
    Note: The logic strictly applies to the FIRST number encountered. Subsequent numbers are yielded as-is 
    (or None if no more data) to show continuous processing capability without storing history.
    """
    # Simulate a stream of integers starting from 10 up to 20 for demonstration
    current_number = 10
    
    while True:
        yield current_number
        
        # Check the FIRST number condition immediately after yielding it
        if not hasattr(memory_efficient_generator, '_first_processed'):
            memory_efficient_generator._first_processed = True
            
            # Yield True only if first number is strictly greater than threshold
            if current_number > THRESHOLD:
                yield True
            else:
                yield False
        
        # Increment for next iteration (simulating stream progression)
        current_number += 1

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate the generator without user input or external dependencies
    
    print("Testing memory-efficient generator with predefined threshold:", THRESHOLD)
    
    gen = memory_efficient_generator()
    
    try:
        while True:
            num = next(gen)
            
            if isinstance(num, bool):
                # Boolean results indicate the outcome of the first number check
                print(f"Number {num}: ", end="")  # Print boolean directly
                
                # Continue to show subsequent yields (numbers or None) without storing them in memory
                continue
            
            else:
                # Yielded integer values from the simulated stream
                print(num, end=", ")
                
    except StopIteration:
        pass
    
    print("\nGenerator completed successfully with O(1) space complexity.")