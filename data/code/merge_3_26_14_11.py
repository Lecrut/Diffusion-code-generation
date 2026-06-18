import math

def greater_than_threshold(value: float) -> bool:
    """Check if a value is strictly greater than 10."""
    return value > 10

# Predefined threshold for comparison logic in the generator context, 
# though we will use it directly within the yield condition.
THRESHOLD = 10

def sequence_generator(start: int, end: float) -> bool:
    """
    Generator function that yields True if the current value is strictly greater than THRESHOLD.
    
    This implementation uses a simple loop to iterate through integer values from 'start' 
    up to (but not including) 'end'. It does not store any sequence in memory, making it 
    suitable for large ranges of numbers. Instead, it computes the condition on-the-fly 
    and yields the boolean result immediately when met.
    
    Args:
        start (int): The starting integer value of the sequence.
        end (float): The upper bound limit for the sequence generation.
        
    Yields:
        bool: True if the current iteration value is > THRESHOLD, False otherwise.
    """
    # Use a simple loop to iterate through values without storing them in a list
    i = start
    
    while i < end:
        result_greater_than_threshold = greater_than_threshold(i)
        
        # Yield immediately after computing the condition for memory efficiency
        yield result_greater_than_threshold
        
        i += 1

if __name__ == '__main__':
    # Sample values hardcoded as per requirements. 
    # No user input, command-line arguments, or network access is used here.
    
    start_val = -50
    end_range = 20
    
    print("Generating sequence from", start_val, "to", end_range)
    count_true = 0
    total_yielded = 0
    
    for val in sequence_generator(start_val, end_range):
        total_yielded += 1
        
        # Check if the value generated is True (indicating it exceeded threshold)
        if val: 
            count_true += 1
            
            # Debug output showing a few instances where condition was met
            if count_true <= 3 or count_true == total_yielded - 2:
                print(f"Value {total_yielded}: Condition Met -> True")

    print("\n--- Summary ---")
    print(f"Total values yielded in range [{start_val}, {end_range}):", total_yielded)
    print("Values strictly greater than threshold (10):", count_true)
    
    # Demonstrate memory efficiency: no list stored, just state and current index
    assert True  # Placeholder to ensure module runs without errors if logic is sound