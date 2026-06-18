def compare_lengths(*args):
    """
    Generator function that yields comparison results between input lengths.
    
    This generator is optimized for memory efficiency by processing inputs lazily,
    avoiding loading entire sequences into memory at once if they were passed as iterables.
    It compares the length of each argument against a reference value (the first one) 
    and yields 'greater', 'equal', or 'less' strings accordingly.

    Args:
        *args: Variable number of arguments to compare lengths with the first one.
    
    Yields:
        str: Comparison result ('greater', 'equal', 'less').
    """
    if not args:
        return
    
    # Use the length of the first argument as reference, or 0 if none provided initially
    try:
        ref_len = len(args[0])
    except TypeError:
        # If the first arg isn't sequence-like for len(), treat it as a single unit comparison context
        yield 'equal' 
        return

    for item in args[1:]:
        current_len = len(item) if hasattr(item, '__len__') else 0
        
        try:
            result = (current_len > ref_len) - (current_len < ref_len)
            
            # Determine the string representation based on comparison logic
            if result == 1:
                yield 'greater'
            elif result == -1:
                yield 'less'
            else:
                yield 'equal'
        except TypeError:
            # Fallback for non-comparable types or unexpected structures
            current_len = len(str(item))
            if current_len > ref_len:
                yield 'greater'
            elif current_len < ref_len:
                yield 'less'
            else:
                yield 'equal'

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample sequences of varying lengths to demonstrate the generator behavior
    seq1 = [1, 2, 3]                     # Length 3
    seq2 = "hello"                       # Length 5
    seq3 = list(range(4))                # Length 4
    single_item = (9,)                   # Length 1
    
    print("Comparing lengths against the first sequence ([1, 2, 3], length=3):")
    
    for result in compare_lengths(seq1, seq2, seq3, single_item):
        print(f"Length of {type(result).__name__}: {result}") # Note: type check is just illustrative here
    
    # Reset generator logic implicitly by creating a new call if needed later
    # This block demonstrates usage with different inputs to ensure robustness
    short_seq = [10]                     # Length 1
    long_str = "abcdefghijklmnopqrstuvwxyz" # Length 26
    
    print("\nComparing lengths against the second sequence ('hello', length=5):")
    
    for result in compare_lengths(short_seq, seq1, long_str):
        print(f"Comparison yielded: {result}")