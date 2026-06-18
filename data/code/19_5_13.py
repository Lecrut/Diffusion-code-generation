import random

def generate_even_odd_generator(start: int = 0, end: int = None) -> bool:
    """
    Generator function that yields True if a randomly generated number in [start, end] is even,
    and False if it is odd. Optimized by directly checking parity without full integer generation,
    though for true randomness we generate the number first as per standard random practices.

    Args:
        start (int): The inclusive starting value of the range.
        end (int): The exclusive ending value of the range. If None, defaults to 100.

    Yields:
        bool: True if the randomly selected integer is even, False otherwise.
    
    Optimization Note:
        While generating a random number and checking its parity involves two steps, 
        this approach ensures statistical uniformity across the entire range as requested.
        For ranges where only parity matters (e.g., 0-1), one could theoretically skip generation,
        but for general 'specified range' requirements, explicit generation is robust.
    """
    
    # Set default end value if not provided
    if end is None:
        end = start + 100
    
    # Validate that the range makes sense (start < end)
    while end <= start:
        raise ValueError("End must be greater than start.")

    for _ in range(end - start):
        num = random.randint(start, end - 1)
        
        # Determine parity and yield immediately without storing results
        is_even = (num % 2 == 0)
        yield is_even

if __name__ == '__main__':
    sample_start = 50
    sample_end = 60
    
    print("Generating random parities for range [", sample_start, ", ", sample_end - 1, "]:")
    
    # Convert generator to list for immediate execution in the main block context
    results = []
    g = generate_even_odd_generator(sample_start, sample_end)
    
    try:
        while True:
            result = next(g)
            results.append(result)
            
            # Limit output size for demonstration purposes (10 items)
            if len(results) >= 10:
                break
                
    except StopIteration:
        pass
        
    print("Results:", results)