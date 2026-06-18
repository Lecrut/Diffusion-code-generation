def find_repeated_letters(text: str) -> set:
    """
    Returns a set of all letters that appear more than once in the input string.
    
    Only alphabetic characters (a-z, A-Z) are considered. Case is treated as 
    distinct unless specified otherwise; however, to provide consistent behavior,
    this implementation treats 'A' and 'a' as different letters based on standard 
    Python set logic over raw characters. If case-insensitive comparison was intended,
    the input could be lowercased first, but per strict interpretation of "letters",
    we count exact character matches unless instructed to normalize.

    Args:
        text (str): The input string to analyze.

    Returns:
        set: A set containing unique letters that appear more than once in `text`.
    
    Example:
        >>> find_repeated_letters("Hello, World!")
        {'l', 'o'}  # Note: H vs h are different; W is not repeated
    
    If case-insensitive behavior is desired for a specific use-case (e.g. "letters" 
    implying regardless of case), the function can be adjusted by converting to lower() first.
    However, without explicit instruction to ignore case, we count exact characters.
    
    Optimization: Uses a single pass with a dictionary or set tracking counts/seen status.
    """
    seen = {}  # Dictionary to track letter occurrences
    
    for char in text:
        if 'a' <= char.lower() <= 'z':  # Check if character is an alphabetic letter (case-insensitive check)
            count = seen.get(char, 0) + 1
            seen[char] = count
            
            # If we encounter a letter that has been seen before and its current count > 1, add to result set.
            # However, since we are building the final set of letters with count > 1 at the end, 
            # we can just track counts and filter later for simplicity or optimize by adding immediately if needed.
            # For maximum efficiency in a single pass without storing all counts then filtering:
            pass

    result = {char for char, count in seen.items() if count > 1}
    
    return result

if __name__ == '__main__':
    sample_strings = [
        "Hello World!",           # Expected: {'l', 'o'} (H!=h) or maybe case-insensitive? Let's assume exact match based on doc. 
                                # Actually, standard interpretation of "letters" often implies case sensitivity unless stated otherwise.
                                # But let's look at the string: H(1), e(1), l(2), o(2), W(1), r(1), d(1). So {'l', 'o'}.
        "A man, a plan, a canal: Panama!",  # Case sensitive: A!=a. 
                                            # Counts: m(3), n(4), p(2), l(2), : (ignored), etc.
                                            # Repeated exact chars: m, n, p, l, :, !? No punctuation requested usually but task says "letters".
                                            # Let's stick to alphabetic only as per logic above. 
                                            # 'm':3, 'n':4, 'p':2, 'l':2 (from plan and canal), a:1 vs A:1 -> distinct.
        "racecar"                 # Expected: {'r', 'a', 'c', 'e'}? No. r(2), a(2), c(2), e(2). All repeated.
    ]

    for test_str in sample_strings:
        print(f"Input: '{test_str}'")
        output = find_repeated_letters(test_str)
        print(f"Repeated letters (exact case): {output}")
        
        # Optional demonstration of case-insensitive behavior if needed, 
        # but the function above handles exact characters.