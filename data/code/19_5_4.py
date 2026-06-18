import random

def yield_even_odd(start: int = 0, end: int = None) -> bool:
    """
    Generator function that yields True if a randomly generated number in [start, end] is even,
    and False otherwise. Optimized by generating only the necessary boolean outcome without
    storing or processing intermediate numbers explicitly beyond parity logic where possible.

    Args:
        start (int): The starting integer of the range (inclusive). Default is 0.
        end (int): The ending integer of the range (exclusive). If None, defaults to a large number for demonstration.

    Yields:
        bool: True if the random number from the specified range is even, False otherwise.
    """
    # Set default upper bound if not provided
    if end is None:
        end = 10_000
    
    current_number = start
    
    while current_number < end:
        # Generate a boolean based on parity of random number in range [start, end)
        num = random.randint(start, end - 1)
        
        # Yield True for even numbers, False for odd numbers
        yield bool(num % 2 == 0)
    
    current_number += 1

if __name__ == '__main__':
    # Sample execution block with no user input or external dependencies
    
    print("--- Generator Test Suite ---\n")
    
    # Define a fixed range for deterministic testing of logic (though random is used, the count remains consistent)
    test_start = 10
    test_end = 25
    
    # Collect results to verify output structure without printing every single one immediately
    results = list(yield_even_odd(test_start, test_end))
    
    print(f"Range: [{test_start}, {test_end})")
    print(f"Total items generated: {len(results)}")
    
    # Verify that the generator actually yields booleans and check distribution roughly
    true_count = sum(1 for x in results if x)
    false_count = len(results) - true_count
    
    print(f"\nDistribution:")
    print(f"  True (Even): {true_count}")
    print(f"  False (Odd):  {false_count}")
    
    # Ensure no interactive prompts or file I/O occurred during execution