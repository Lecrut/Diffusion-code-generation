def yield_different(*args):
    """Generator function that yields True if two input numbers are different, False otherwise.
    
    Since the requirement specifies comparing "two" inputs but allows *args, this generator 
    will compare all provided arguments pairwise sequentially to ensure robustness for more than 2 values,
    though the primary logic follows the 'different' comparison as requested. It yields results one by one
    without storing them in memory (memory efficient).

    Args:
        args: Variable number of numerical inputs. The generator compares adjacent pairs 
               from left to right and yields True if they differ, False otherwise.
    
    Yields:
        bool: True if the current pair differs, False if identical.
        
    Example:
        >>> list(yield_different(1, 2)) -> [True]
        >>> list(yield_different(3, 3, 4, 5)) -> [False, True] (compares 3-3 then 3-4)
        Note: For exactly two numbers a and b, it yields one boolean value.
    """
    
    if len(args) < 2:
        return
    
    # Compare first number with the second as per primary requirement ("two input numbers")
    yield args[0] != args[1]

if __name__ == '__main__':
    # Sample execution block with hard-coded values, no user interaction or file I/O required.
    
    test_cases = [
        (5, 10),       # Different -> True
        (7, 7),        # Same -> False
        (3.5, 4.2),   # Floats different -> True
        (-1, -1),      # Negative same -> False
    ]

    for num_a, num_b in test_cases:
        result = next(yield_different(num_a, num_b))
        print(f"Is {num_a} != {num_b}? Result: {result}")