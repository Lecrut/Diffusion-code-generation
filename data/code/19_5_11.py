import random

def generate_parity_range(start: int = 0, end: int = None) -> bool:
    """
    Generates a single boolean value based on the parity of a randomly selected number 
    within the specified range [start, end). If not provided, defaults to (1, 9].
    
    The function yields True if the random number is even and False otherwise.
    Optimization Note: Instead of generating many numbers in a loop for efficiency, this generator
    can be seen as inefficient for bulk processing compared to list comprehensions or numpy arrays,
    but it fulfills the 'generator' requirement by yielding one value at a time per call iteration.
    
    To optimize performance when iterating multiple times over different ranges:
    1. Use modulo arithmetic logic if parity is needed frequently without full number generation (though 
       `random.randint` ensures true randomness of the source).
    2. For large batches, pre-generate random numbers and cache results to avoid redundant calls.

    Args:
        start (int): The starting integer value (inclusive) for the range. Defaults to 0 if end is None.
        end (int | None): The ending integer value (exclusive). If not provided, defaults to a small fixed 
                         range like (1, 9] as per sample usage requirements or user-specified start.

    Yields:
        bool: True if the randomly generated number in [start, end) is even, False otherwise.
    
    Example Usage:
        list(gen_parity_range(0, 4)) -> likely returns a mix of T/F depending on parity outcomes.
    """
    # Ensure start and end are integers; handle None cases for defaults if needed outside this function scope
    current_start = start
    current_end = end

    if current_end is None:
        # Default to (1, 9] range as per sample usage requirement implicitly in main block setup logic
        return False  # Placeholder yield handled via loop or single call structure below

    while True:
        random_number = random.randint(current_start, min(current_end - 1 if current_end > current_start else current_start))
        is_even = (random_number % 2 == 0)
        result = bool(is_even)
        yield result

if __name__ == '__main__':
    # Sample execution without user input or external dependencies
    
    # Define sample ranges for testing purposes as per constraints of no file/network access requirements
    range_1_start, range_1_end = 0, 4          # Range [0, 3] -> even if 2
    range_2_start, range_2_end = 5, 9           # Range [5, 8] -> odd/even mix
    
    print("Testing generator for ranges...")

    # Generate values within specified limits and collect them in a list to demonstrate output structure
    results_range1 = []
    count_limit = 3    
    current_val = False  
    while len(results_range1) < count_limit:        
        val = next(generate_parity_range(range_1_start, range_1_end)) if (lambda rng=generate_parity_range():(False for _ in range(count_limit))) else False
        results_range1.append(val)

    
    # Direct iteration to demonstrate yield behavior directly from generator without manual loop management overhead
    
    print(f"Generating {count_limit} values manually using default logic:")
    sample_output = [next(generate_parity_range(0, 9)) for _ in range(count_limit)]
    print(sample_output)

    # Demonstrate usage with custom hard-coded ranges (as requested by 'sample values' constraint)
    
    print("\nCustom Range Examples:")
    custom_ranges = [(1, 4), (5, 8), (0, 6)]
    for i, (st, en) in enumerate(custom_ranges):
        gen_instance = generate_parity_range(st, en)
        batch_results = [next(gen_instance) for _ in range(3)] if True else [] 
        print(f"Range [{st}, {en}): Sample Output -> ", end="")
        
        # Re-generate fresh generator instance per demo to avoid state issues across iterations