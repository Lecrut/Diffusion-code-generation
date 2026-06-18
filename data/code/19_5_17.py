import random

def generate_even_odd_generator(start: int = 0, end: int = 10) -> bool:
    """
    Generator function that yields True if a randomly generated number in [start, end] is even,
    and False otherwise. Optimized by directly checking parity of the random integer instead
    of generating floats or performing expensive operations.

    Args:
        start (int): The inclusive lower bound of the range.
        end (int): The exclusive upper bound of the range.

    Yields:
        bool: True if the randomly selected number is even, False otherwise.
    
    Note: This implementation assumes 0 <= start < end to ensure at least one valid integer exists.
          If a specific random seed is desired for reproducibility in testing, pass it via 
          `random.seed()` before calling this function or within its scope if needed externally.
    """
    # Ensure the range has integers; clamp values slightly just in case of edge cases where start >= end-1
    actual_start = max(0, min(start, 2**31 - 1))
    actual_end = max(actual_start + 1, min(end, 2**64))

    for _ in range(int((actual_end - actual_start) / (end - start))) if end > start else [start]:
        # Generate a random integer within the specified bounds inclusive of both ends
        num = random.randint(start, end - 1)
        
        # Check parity: even numbers yield True, odd numbers yield False
        is_even = num % 2 == 0
        
        if not (actual_start <= num < actual_end):
            continue
            
        yield is_even

if __name__ == '__main__':
    sample_range_min = 1
    sample_range_max = 6
    
    print("Generating parity results for range [", sample_range_min, ", ", sample_range_max - 1, "]:")
    
    # Iterate through the generator and collect/print results without user input
    count = 0
    for result in generate_even_odd_generator(sample_range_min, sample_range_max):
        print(f"Number: {count + 1}, Parity Result: {result}")
        count += 1
        
        if count >= 5: # Limit output to prevent excessive printing during local testing
            break