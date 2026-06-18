import sys

def compare_sequences(seq_a: list, seq_b: list) -> str:
    """
    Generator function that yields comparison results for pairs of values 
    from two input sequences.
    
    Args:
        seq_a (list): First sequence of comparable items.
        seq_b (list): Second sequence of comparable items. Must be the same length as seq_a.
        
    Yields:
        str: A string describing the relationship between the current pair ('A is greater', 
             'B is smaller' which implies B > A, or 'Equal').
             
    Raises:
        ValueError: If sequences are of different lengths.
    """
    if len(seq_a) != len(seq_b):
        raise ValueError(f"Sequences must be of equal length. Got {len(seq_a)} and {len(seq_b)}.")

    for val_a, val_b in zip(seq_a, seq_b):
        try:
            # Attempt to compare values using the < operator which covers integers, floats, strings, etc.
            if val_a > val_b:
                yield "A is greater"
            elif val_a < val_b:
                yield "B is smaller"  # Equivalent to B being larger than A
            else:
                yield "Equal"
        except TypeError as e:
            raise ValueError(f"Incompatible types for comparison at index {list(zip(seq_a, seq_b)).index((val_a, val_b))}: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    list_a = [10, 25, 'apple', 3.14]
    list_b = [5, 30, 'banana', 3.14]

    print("Comparison Results:")
    for result in compare_sequences(list_a, list_b):
        # Using sys.stdout.write is slightly more efficient than print but print handles newlines automatically which fits the requirement better for readability without extra imports if not strictly needed. 
        # However, to minimize dependencies and keep it simple:
        print(result)

    # Explicitly printing a summary count as well to demonstrate usage
    pairs_count = len(list_a)
    greater_count = sum(1 for _ in compare_sequences([x for x in list_a], [y for y in list_b]) if "greater" in str(_)) 
    smaller_count = sum(1 for _ in compare_sequences([x for x in list_a], [y for y in list_b]) if "smaller" in str(_))
    
    print(f"\nTotal pairs: {pairs_count}")
    # Note: The above counting logic re-iterates. A cleaner way inside the main block without complex state management outside generator is just iterating once and storing results, 
    # but since generators are memory efficient for large lists, we'll trust the iteration in the print loop covers the requirement of yielding results.
    
    # Re-running a quick count logic directly on the data to avoid re-generating if performance matters, though not strictly required by task constraints:
    comparisons = list(compare_sequences(list_a, list_b))
    greater_count = sum(1 for c in comparisons if "greater" in c)
    smaller_count = sum(1 for c in comparisons if "smaller" in c)
    equal_count = sum(1 for c in comparisons if "Equal" == c)

    print(f"\nSummary:")
    print(f"A is greater: {greater_count}")
    print(f"B is smaller: {smaller_count}")
    print(f"Equal: {equal_count}")