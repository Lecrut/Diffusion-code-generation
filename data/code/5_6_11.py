import sys

def compare_lengths(*args):
    """
    Generator function that yields comparison results between input lengths.
    
    This generator takes any number of arguments (sequences or iterables) and 
    compares their lengths pairwise in a memory-efficient manner for large inputs.
    It does not load the entire sequences into memory at once; instead, it uses
    len() which is optimized by Python to compute length without full traversal 
    if possible (e.g., for lists), but even then avoids holding references to all items.

    Args:
        *args: Variable number of iterables or values whose lengths are compared.
    
    Yields:
        int: 1 if the first argument is longer than the second, -1 if shorter, 
             and 0 if equal length (compares arg[0] vs arg[1], then arg[2] vs arg[3], etc.).

    Note: For very large sequences where len() might be expensive or unavailable,
        this function assumes standard Python behavior. If memory efficiency is critical
        for streaming data without knowing the total length upfront, a custom iterator-based approach 
        would require buffering which contradicts "no full load". Here we use built-in len().

    Example:
        >>> list(compare_lengths([1], [2]))
        [-1]  # len(1) < len(2)
        >>> list(compare_lengths("abc", "ab"))
        [1]   # len(3) > len(2)
    """
    if not args:
        return

    # Group arguments into pairs for comparison (first vs second, third vs fourth, etc.)
    iterator = iter(args)
    
    while True:
        try:
            first_arg = next(iterator)
            second_arg = next(iterator)
            
            len1 = len(first_arg)
            len2 = len(second_arg)
            
            if len1 > len2:
                yield 1
            elif len1 < len2:
                yield -1
            else:
                yield 0
                
        except StopIteration:
            # If an odd number of arguments were passed, the last one is ignored 
            # as there's no pair to compare it with. This maintains memory efficiency.
            break

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample 1: Two lists of different sizes
    result_sample_1 = list(compare_lengths([1, 2], [3]))
    
    # Sample 2: Strings with equal length
    result_sample_2 = list(compare_lengths("hello", "world"))
    
    # Sample 3: Mixed types (list and tuple) where lengths differ significantly
    result_sample_3 = list(compare_lengths([1, 2, 3], [4]))
    
    # Print results to verify functionality
    print(f"Sample 1 (len {len(result_sample_1)}): {result_sample_1}")
    print(f"Sample 2 (len {len(result_sample_2)}): {result_sample_2}")
    print(f"Sample 3 (len {len(result_sample_3)}): {result_sample_3}")

    # Additional test with many arguments to ensure pairing logic works correctly
    samples = [range(i) for i in range(10)] + ["test"] * 5
    result_many = list(compare_lengths(*samples))
    print(f"Sample Many (len {len(result_many)}): {result_many}")

    # Verify correctness of basic cases manually if needed during development, 
    # but here we just output the results as per task requirements.