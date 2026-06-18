import random

def generate_even_odd_generator(start: int = 0, end: int = None) -> bool:
    """
    Generator function that yields True if a randomly generated number in range [start, end] is even,
    and False otherwise. Optimized by pre-calculating the parity of each number to avoid redundant modulo operations.

    Args:
        start (int): The starting integer for the random generation (inclusive).
        end (int): The ending integer for the random generation (exclusive). If None, defaults to 100.

    Yields:
        bool: True if a randomly selected number in the range is even, False otherwise.
    
    Note: This implementation uses pre-computed parity lookup tables for optimal performance over large ranges.
    """
    # Set default end value if not provided
    if end is None:
        end = 100

    # Ensure start and end are integers (though input() restrictions mean we assume valid int inputs)
    start = int(start)
    end = int(end)

    # Validate range to ensure a non-empty sequence
    if start >= end:
        return

    # Create parity lookup table for the entire range [start, end)
    # This avoids repeated modulo calculations during iteration.
    parities = [(n % 2 == 0) for n in range(start, end)]

    # Generate random indices within the valid index range of our pre-computed list
    total_numbers = len(parities)
    
    while True:
        yield random.choice(parities)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments.
    start_val = 10
    end_val = 25
    
    print(f"Generating parity results in range [{start_val}, {end_val}):")
    
    count_even = 0
    count_odd = 0
    total_yielded = 0
    
    for is_even in generate_even_odd_generator(start=start_val, end=end_val):
        if is_even:
            count_even += 1
        else:
            count_odd += 1
        total_yielded += 1
        
        # Print every 5th result to avoid excessive output volume while demonstrating functionality.
        if total_yielded % 5 == 0 or total_yielded == len(list(range(start_val, end_val))):
            print(f"Yielded: {is_even} (Count Even: {count_even}, Count Odd: {count_odd})")

    # Final summary line after loop completes naturally based on range size.
    if count_even > 0 or count_odd > 0:
        final_print = f"\nFinal Counts - Even: {count_even}, Odd: {count_odd}"
        print(final_print)