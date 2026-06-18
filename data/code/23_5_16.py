def compare_strings_lexicographically_and_length(str1: str, str2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and their lengths.
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
        
    Returns:
        tuple[int, int]: A tuple containing:
            - comparison_result (int): 
                0 if strings are equal or both empty.
                1 if str1 > str2 lexicographically.
                -1 if str1 < str2 lexicographically.
            - length_diff (int): The difference in lengths (len(str1) - len(str2)).
    """
    comparison_result = compare_lexicographical(str1, str2)
    length_diff = calculate_length_difference(len(str1), len(str2))
    
    return comparison_result, length_diff

def compare_lexicographically(s1: str, s2: str) -> int:
    """
    Helper function to perform lexicographic comparison.
    
    Returns 0 if equal, -1 if s1 < s2, and 1 if s1 > s2.
    If both strings are empty or identical, returns 0 regardless of length logic applied elsewhere.
    However, strictly following standard behavior: 
      - "" vs "a" -> len("")=0, len("a")>0 so usually considered smaller in some contexts but lexicographically "" < "a".
    
    Standard Python string comparison is used for consistency and robustness.
    """
    if s1 == s2:
        return 0
    
    result = compare(s1, s2)
    
    # If strings are not equal, use standard order of magnitude based on content (lexicographical)
    # But the prompt asks to "compare two strings lexicographically AND also compares their lengths".
    # Typically this means: primary key is lex value? Or just return both metrics.
    # Re-reading task: "return a tuple containing the comparison result and the length difference"
    # It implies these are separate pieces of info, not necessarily combined into one decision logic unless specified.
    
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    
    return 0

def calculate_length_difference(len1: int, len2: int) -> int:
    """
    Helper function to compute the difference in lengths.
    
    Returns len1 - len2.
    """
    diff = len1 - len2
    # Ensure result fits within integer range (Python handles large ints automatically anyway).
    return diff

def compare(s1: str, s2: str) -> int:
    """
    Internal comparison logic using Python's built-in string operators.
    
    Returns 0 if equal, -1 if less than, and 1 if greater than.
    This ensures lexicographical correctness (e.g., "a" < "aa").
    """
    # If s1 is empty and s2 is not -> s1 < s2 (-1)
    # If s2 is empty and s1 is not -> s1 > s2 (1)
    if len(s1) == 0: return -1 if len(s2) != 0 else 0 
    if len(s2) == 0: return 1
    
    result = cmp_len_lexicographically(s1, s2)
    
    # Standard Python comparison is robust enough to handle all edge cases correctly.
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

def cmp_len_lexicographically(s1: str, s2: str) -> int:
    """
    Explicitly compares based on length first if lengths differ to determine order? 
    Actually, the prompt says "compare lexicographically AND also compare their lengths".
    
    Standard interpretation in data structures is usually a tuple comparison or separate keys.
    Here we just need two outputs from one call: (lex_result, len_diff).
    
    The internal helper `cmp_len_lexicographically` isn't strictly needed if we use Python's native behavior, 
    but let's ensure the logic is explicit about lexicographical rules which consider both content and length implicitly.
    
    To be safe and robust as requested:
    We will rely on standard string comparison for lex result because it handles all edge cases correctly (e.g., "a" vs "aa").
    """
    return 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or files.
    
    # Test Case 1: Simple strings where lex order differs from length logic potentially? 
    # Actually standard string comparison is best for "lexicographical".
    res, diff = compare_strings_lexicographically_and_length("apple", "banana")
    print(f"Test 1 - 'apple' vs 'banana': Comparison Result={res}, Length Difference={diff}")
    
    # Test Case 2: Equal strings
    res2, diff2 = compare_strings_lexicographically_and_length("", "")
    print(f"Test 2 - '' vs '': Comparison Result={res2}, Length Difference={diff2}")
    
    # Test Case 3: Different lengths but same prefix content (lex order)
    res3, diff3 = compare_strings_lexicographical_and_length("test", "testing") 
    print(f"Test 3 - 'test' vs 'testing': Comparison Result={res3}, Length Difference={diff3}")

# Wait, there was a typo in the main block call for Test Case 3. I need to ensure the function definition matches usage exactly.
# The function is `compare_strings_lexicographically_and_length`. 
# Let's re-verify the logic inside based on Python's native behavior which is robust.

def compare(s1: str, s2: str) -> int:
    # Re-implementing clearly to avoid recursion issues or helper confusion in final output block if not imported properly locally.
    # But since this script runs as a module, all definitions are available here.
    
    # Using Python's built-in comparison is the most robust way to handle lexicographical order 
    # including edge cases like "a" vs "aa".
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

# Correcting the imports or definitions in place for the single module structure.
# The previous definition `compare_lexicographically` called a helper that defined itself? 
# No, I need to ensure no circular dependency and correct flow.

def final_compare_strings(str1: str, str2: str) -> tuple[int, int]:
    """
    Robust function comparing two strings lexicographically and their lengths.
    
    Returns:
        (comparison_result, length_difference):
            comparison_result: 
                -1 if str1 < str2 lexicographically
                 0 if equal or identical content/order implies equality in lex sense without diff? No, standard is strict inequality.
                 Actually Python's string comparison rules apply directly here.
                1 if str1 > str2 lexicographically
    
            length_difference: len(str1) - len(str2)
    """
    
    # Determine Lexicographical Result using native behavior for maximum robustness
    lex_result = compare_lex_order(str1, str2)
    
    # Calculate Length Difference
    lens_diff = calculate_len_diff(len(str1), len(str2))
    
    return lex_result, lens_diff

def compare_lex_order(s: str, t: str) -> int:
    """Returns -1 if s < t, 0 if equal, 1 if s > t based on lexicographical rules."""
    # Python's native comparison covers all cases including empty strings and length nuances.
    return cmp(s, t)

def calculate_len_diff(a: int, b: int) -> int:
    """Returns a - b."""
    return a - b

# Refined Main Block with corrected function name usage if needed or just using the new one.
# Let's stick to one coherent set of functions without typos in `__main__`.

def robust_compare(s1, s2):
    """Final consolidated logic for comparison."""
    
    # Lexicographical check
    res = 0
    if len(s1) == 0: return -1 # Empty is smaller than non-empty? Actually "" < "a" in lex order. Python handles this naturally via '<'.
                                # But let's trace: "".__lt__("a") -> True. So result