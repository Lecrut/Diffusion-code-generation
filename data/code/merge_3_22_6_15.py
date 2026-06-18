def odd_even_generator(start: int = 1, end: int = None) -> bool:
    """
    Generator function that yields True if a number is even, False otherwise.
    
    Args:
        start (int): The starting integer of the range (inclusive).
        end (int): The ending integer of the range (exclusive). Defaults to 100 for efficiency demonstration without hard limits.

    Yields:
        bool: True if the current number is even, False otherwise.
    
    Memory Efficiency Note:
        This function uses a generator which processes numbers one at a time,
        storing only state in local variables rather than creating lists or arrays.
    """
    # If end is not provided, default to 100 for the sample run logic if needed later, 
    # but here we allow dynamic ranges as per task description flexibility.
    if end is None:
        raise ValueError("End value must be provided when calling this function directly.")

    current = start
    
    while True:
        yield (current % 2 == 0)
        
        try:
            # Check for StopIteration manually to allow controlled iteration in main block without exception handling overhead inside generator logic if desired, 
            # but standard range usage is cleaner. Let's switch to a simpler loop structure based on input arguments directly.
            pass
        except Exception:
            break
            
    # Re-implementing with explicit stop condition for clarity and robustness against infinite loops in testing scenarios without external inputs.

def odd_even_generator_v2(start: int, end: int) -> bool:
    """
    Generator function that yields True if a number is even, False otherwise.
    
    Args:
        start (int): The starting integer of the range (inclusive).
        end (int): The ending integer of the range (exclusive).

    Yields:
        bool: True if the current number is even, False otherwise.
    """
    for num in range(start, end):
        yield num % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (1 to 20)
    start_num = 1
    end_num = 20
    
    print("Odd/Even Check Results for range [", start_num, ", ", end_num, "):")
    
    results = odd_even_generator_v2(start_num, end_num)
    
    # Iterate through the generator to demonstrate memory efficiency (no list storage in main scope before printing)
    count = 0
    while True:
        try:
            is_even = next(results)
            num = start_num + count
            
            if is_even:
                print(f"{num}: Even")
            else:
                print(f"{num}: Odd")
            
            count += 1
            # Stop after processing the full range to ensure termination without infinite loops in test environments
        except StopIteration:
            break
    
    print("\nGenerator completed successfully.")