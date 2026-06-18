import random

# Predefined threshold value
THRESHOLD = 50

def memory_efficient_generator():
    """
    Generator function that yields True if a randomly generated number 
    is strictly greater than THRESHOLD, and False otherwise.
    
    Designed for memory efficiency by yielding one boolean at a time 
    without storing the entire sequence in memory.
    """
    while True:
        # Generate a random integer between 0 and 100 (inclusive)
        number = random.randint(0, 100)
        
        if number > THRESHOLD:
            yield True
        else:
            yield False

if __name__ == '__main__':
    # Sample execution block with hard-coded values for demonstration
    
    print("Testing memory-efficient generator...")
    
    # Create an iterator from the generator (no list storage)
    gen = memory_efficient_generator()
    
    # Yield and check first 5 results to demonstrate functionality
    count = 0
    while True:
        result = next(gen, None)
        
        if result is not None:
            print(f"Result {count + 1}: {result}")
            
            # Stop after checking the first 3 values for brevity in this demo
            if count >= 2:
                break
            
            count += 1
        
        # Safety check to prevent infinite loop on error
        else:
            print("Generator exhausted or raised an exception.")
            break
    
    print("\nNote: The generator continues yielding indefinitely unless stopped manually.")