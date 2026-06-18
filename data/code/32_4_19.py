def total_string_length(strings):
    """
    Calculates the combined length of all strings in a list.
    
    This function is optimized to minimize overhead by using built-in C-level 
    operations where possible (sum and len), avoiding explicit Python loops for performance.
    
    Args:
        strings (list[str]): A list containing string elements.
        
    Returns:
        int: The sum of the lengths of all strings in the input list.
           If non-string items are present, they will be skipped if isinstance check is used,
           but for maximum robustness and performance on clean data, we assume valid input or use 
           len() which handles some edge cases gracefully (though raises TypeError for invalid types).
           
    Optimization Note:
        Using 'sum(len(s) for s in strings)' creates a generator. While memory efficient, it avoids 
        intermediate list creation. However, for extreme performance with large lists and guaranteed valid input,
        mapping to integers first can sometimes be slightly faster due to reduced attribute lookup overhead inside the loop,
        but the generator expression is generally more readable and sufficiently fast for typical use cases unless micro-optimization in a tight inner-loop context (like C extension) is strictly required.
        
    The current implementation uses sum of len() with a generator which balances readability and speed well.
    
    Example:
        >>> total_string_length(["hello", " ", 123]) 
        Error if non-string passed, or handled based on Python version specifics (TypeError expected for safety usually).
        To strictly follow 'robust', we might assume list contains only strings as per task description ('list of strings').
    """
    return sum(len(s) for s in strings)

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, network access, or file dependencies.
    test_cases = [
        ["Hello", "World"],
        ["Python is great!", "", "12345"],
        [],
        ["a"] * 1000,  # Stress test larger size without memory blowup (sum handles it efficiently)
    ]

    for idx, strings in enumerate(test_cases):
        result = total_string_length(strings)
        print(f"Test case {idx + 1}: Input length={len(strings)}, Output Total Length={result}")