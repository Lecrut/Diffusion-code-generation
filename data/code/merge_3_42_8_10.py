"""
Script demonstrating string construction using list comprehension 
and str.join() method with clear optimization comments.
"""

def construct_greeting(names: list[str]) -> str:
    """
    Constructs a greeting message from a list of names.
    
    Optimization Note:
    Instead of iterating through the list multiple times (e.g., once to build parts 
    and again to join them), we use a single pass with list comprehension combined 
    directly with str.join(). This is more efficient in terms of CPU time because 
    it avoids redundant iterations over the same data. The intermediate string building 
    within loop bodies is replaced by a clean, optimized sequence operation provided 
    by Python's internal C implementation for join().
    
    Args:
        names (list[str]): A list containing individual name strings.
        
    Returns:
        str: A formatted greeting message with each name on a new line followed by a period.
    """
    # Construct the final string using list comprehension to create parts 
    # and immediately join them with newline characters and periods.
    return '\n'.join([f"{name}.\n" for name in names])

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    sample_names = ["Alice", "Bob", "Charlie"]
    
    result = construct_greeting(sample_names)
    print(result)