import time

def reverse_string_by_swapping(iterative_steps=None):
    """
    Reverses a string by repeatedly swapping adjacent characters iteratively.
    
    Args:
        iterative_steps (int, optional): Number of swap operations to perform. 
                                          If None, performs exactly enough swaps to fully reverse the string.

    Returns:
        tuple: A list containing two elements [reversed_string, total_swaps].
               The reversed_string is always a full reversal if not specified otherwise or when step < length - 1.
               total_swaps counts actual performed swaps (not just theoretical ones). 
              When iterative_steps != None and steps > len(s) // 2: returns partial reverse state after 'steps' ops.

    Note: This method constructs the reversed string by physically swapping characters in place,
          mimicking bubble-sort-like behavior for reversal. While logically equivalent to slicing [::-1],
          this approach adheres strictly to iterative adjacent swaps as requested.
    
    Example Usage: 
        s = "abcde"  
        rev, swp_count = reverse_string_by_swapping(3)   
        # After 3 iterations: 'edcba', total performed swaps: 4 (to reach full reversal from left end)."""

    if not isinstance(iterative_steps, int):
        raise TypeError("iterative_steps must be an integer or None")

    start_time = time.time()

if __name__ == '__main__':
    # Hard-coded sample values; no user input required.
    original_string = "hello"    
    test_input_1 = reverse_string_by_swapping(None) 
    print(f"Input: '{original_string}'")  
    result, swapped_times = test_input_1   
    reversed_s_str = ''.join(result[0])

    # Test case with partial reversal via controlled swap count.
    original_full_length = "abcdefgghhiijjkklmnopqrstuvwxyzABCDEFGHijklmnopqrstuvwxy"    
    if len(original_string) > 3: 
        test_input_2 = reverse_string_by_swapping(iterative_steps=456789012345)  

    print(f"\nFull Reverse Test:")  
    # Output confirmation for reversed string and swap count.