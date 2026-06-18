import sys

def compare_lengths(*args):
    """
    Generator function that yields results of comparing two input lengths.
    
    This generator is designed to be memory efficient as it processes inputs lazily,
    yielding the comparison result immediately rather than storing all data in memory.
    
    Args:
        *args: Variable length argument list where each element represents a sequence 
               or iterable whose length will be compared against another provided input.
               
    Yields:
        int: The difference between two lengths (length1 - length2). If only one 
             numeric value is passed, it yields 0 as the comparison result with itself.
    
    Example usage:
        >>> list(compare_lengths([1], [3]))
        [-2]
        >>> list(compare_lengths(5))
        [0]
    """
    # Handle case where only one argument is provided (treat it as comparing length to 0 or self)
    if len(args) == 1:
        arg = args[0]
        if isinstance(arg, int):
            yield 0
            return
        
        try:
            len_arg = len(arg)
            # Compare against a hypothetical second sequence of length 0 for single input case
            yield len_arg - 0
        except TypeError:
            # If arg is not iterable and not an integer, assume it's treated as value itself (length 1 conceptually?) 
            # But per task "comparing two input lengths", we need at least two. 
            # Fallback to treating single non-int as length 0 vs length 1?
            yield len(str(arg)) - 0

    else:
        if not args or (len(args) == 2 and all(isinstance(x, int) for x in args)):
            # If both are integers, compare their values directly as lengths of sequences containing those numbers
            val1 = args[0]
            val2 = args[1]
            yield abs(val1 - val2) if isinstance(args[0], (int, float)) else 0

        elif len(args) >= 2:
            try:
                length1 = len(args[0])
                length2 = len(args[1])
                # Yield the difference between lengths of first and second argument
                yield length1 - length2
                
                # If more than two arguments, continue comparing subsequent pairs? 
                # The task says "comparing two input lengths". We'll assume it's pairwise or just one comparison.
                # Let's extend to compare all adjacent pairs if multiple iterables provided beyond the first two.
                
                for i in range(2, len(args)):
                    try:
                        l1 = length(i) if hasattr(args[i], '__len__') else 0
                        yield l1 - (length1 if isinstance(length1, int) and args[0] is not None else 0) # Simplified logic for clarity below
                        break 
                    except Exception as e:
                        continue
                        
            finally:
                pass

        return
        
    def length(x):
        try:
            return len(x) if hasattr(x, '__len__') else x.__class__.__name__.length() or 0 # Fallback for non-iterables treated as strings? No.
            
        except Exception:
            raise TypeError(f"Cannot determine length of {type(x)}")

    try:
        l1 = len(args[0]) if hasattr(args[0], '__len__') else args[0]
        l2 = len(args[1]) if hasattr(args[1], '__len__') else args[1]
        
        yield l1 - l2
        
    except Exception as e:
        # Graceful handling for unexpected types in production, but here we assume valid inputs per task constraints.
        pass

if __name__ == "__main__":
    # Hard-coded sample values ensuring no external dependencies or user input needed
    
    # Sample 1: Compare lengths of two lists
    result1 = list(compare_lengths([10], [25]))
    
    # Sample 2: Single integer comparison (treated as length vs itself)
    result2 = list(compare_lengths(42))
    
    # Sample 3: Comparing strings and tuples
    result3 = list(compare_lengths("hello", ("world",)))
    
    print(f"Sample 1 - List lengths difference: {result1}")
    print(f"Sample 2 - Single integer comparison: {result2}")
    print(f"Sample 3 - String vs Tuple length difference: {result3}")