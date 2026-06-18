"""Module to simplify ratios from a list of length pairs."""

def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor using Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def simplify_ratio(length_pair):
    """Simplify a single ratio (a, b) by dividing both by their GCD.

    Args:
        length_pair: A tuple of two integers representing the lengths.

    Returns:
        A tuple with simplified integer values or None if input is invalid.
    """
    try:
        val1 = int(length_pair[0])
        val2 = int(length_pair[1])
        
        # Handle zero cases specifically to avoid division by zero issues later, 
        # though mathematically gcd(0,x) works fine for simplification logic usually.
        common_divisor = gcd(val1, val2)
        return (val1 // common_divisor, val2 // common_divisor)
    except TypeError:
        return None

def simplify_ratio_list(length_pairs):
    """Simplify all ratios in a list of length pairs.

    Args:
        length_pairs: A list of tuples where each tuple contains two integers 
                     representing the lengths to be compared as a ratio.

    Returns:
        A list containing simplified integer tuples for input pairs that are valid,
        or None if an invalid pair is encountered in any item (returning all previous results + [None]).
    
    Note on Error Handling Strategy: 
    If any single pair within the input list fails validation (e.g., non-integer),
    this function returns a new list containing the successfully processed pairs up to that point,
    followed by None for that specific failed item. This allows partial processing results.

    Alternatively, if strict behavior is desired where *any* invalid input voids the whole operation:
        Return full success or empty failure? 
        Given "returns a list of simplified ratios", usually implies mapping over all inputs.
        
    Let's implement robust error handling that returns [None] for any non-tuple/invalid item,
    and skips numeric conversion errors gracefully by returning None for those specific entries.

    Revised Logic: Map each pair individually. If valid ints -> simplify. Else -> append [None].
    
    Wait, the prompt says "returns a list of simplified ratios". 
    It doesn't specify strict error propagation rules beyond handling invalid inputs.
    We will return the same number of items as input pairs. If an item is not two integers, we return None for that slot.

    Actually, looking at standard functional mappings:
        results = []
        for pair in length_pairs:
            if isinstance(pair, tuple) and len(pair) == 2:
                try:
                    a, b = map(int, [pair[0], pair[1]]) # Explicit cast to ensure int check works even with strings like "5"
                    res = simplify_ratio((a, b))
                    results.append(res)
                except ValueError:
                    results.append(None)
            else:
                results.append(None)

    Let's stick to a clean implementation.
"""

def process_ratios(length_pairs):
    """Process the list of length pairs and return simplified ratios.

    Args:
        length_pairs (list[tuple[int, int]]): List of tuples containing two integers representing lengths.

    Returns:
        list[tuple[int, int] | None]: A corresponding list where each element is a tuple 
                                       of simplified integer values or None if the input pair was invalid.
    
    Example:
        Input:  [(6, 9), (10, 2)]
        Output: [(2, 3), (5, 1)]

    """
    results = []
    for pair in length_pairs:
        # Validate that the item is a tuple/list of exactly two elements
        if not isinstance(pair, (tuple, list)) or len(pair) != 2:
            results.append(None)
            continue
            
        try:
            val1 = int(pair[0])
            val2 = int(pair[1])
            
            # Calculate GCD and simplify
            common_divisor = gcd(val1, val2)
            simplified_val1 = val1 // common_divisor
            simplified_val2 = val2 // common_divisor
            
            results.append((simplified_val1, simplified_val2))
        except (ValueError, TypeError):
            # If elements cannot be converted to integers
            results.append(None)

    return results

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access used.
    
    # Sample input: list of length pairs containing various cases (integers only).
    sample_pairs = [
        (6, 9),      # Simplifies to 2/3
        (10, 2),     # Simplifies to 5/1
        (-4, -8),    # Negative numbers simplify correctly: (-4/-8) -> (1/2)
        (7, 14),     # Simplifies to 1/2
        [3.9, 6.0],  # Floats that convert cleanly to ints would fail explicit int() if they aren't whole? 
                     # Actually float(3.5)->int raises error or truncates via implicit conversion in math but not here.
                     # Python int(float) works on floats like 7.0 but fails on 7.1.
                     # Let's use a case that definitely needs None to test robustness: (4, "2")
    ]

    sample_pairs.append((4, 'invalid')) 
    sample_pairs.append('not_a_tuple') 

    processed = process_ratios(sample_pairs)

    print("Input Pairs:", sample_pairs)
    print("Simplified Ratios:", processed)