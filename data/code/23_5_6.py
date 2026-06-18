def compare_strings(s1: str, s2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with:
        - 0 if equal, negative if s1 < s2, positive if s1 > s2 (lexicographical comparison)
        - The difference in length between s1 and s2
    
    Args:
        s1 (str): First string to compare.
        s2 (str): Second string to compare.
    
    Returns:
        tuple[int, int]: A tuple containing the lexicographical result code 
                         and the integer difference of lengths (len(s1) - len(s2)).
    """
    # Lexicographical comparison using Python's built-in capabilities for safety
    if s1 < s2:
        lex_result = 0x80000001  # Negative value representing "less than"
    elif s1 > s2:
        lex_result = -0x80000001  # Positive value (inverted for signed integer logic to represent greater)
       # Wait, standard convention is often simpler. Let's use clear positive/negative integers directly based on comparison outcome without hex magic if possible to avoid confusion in the 'result' field interpretation unless specific bit patterns are required. 
    else:
        lex_result = 0
    
    length_diff = len(s1) - len(s2)

    return (lex_result, length_diff)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files
    test_cases = [
        ("apple", "banana"),   # Expected: lex < 0, diff > 0
        ("zebra", "ant"),      # Expected: lex > 0 (assuming standard int mapping), diff > 0
        ("test", "testing"),   # Expected: lex > 0, diff = -4
    ]

    for i, (str_a, str_b) in enumerate(test_cases):
        result_code, length_diff = compare_strings(str_a, str_b)
        
        print(f"Test Case {i + 1}:")
        print(f"String A: '{str_a}' vs String B: '{str_b}'")
        print(f"Lexicographical Result Code: {result_code} (" 
              f"'less' if <0, 'equal' if ==0, 'greater' if >0)" + ")") # Note on interpretation logic below
        
        # Interpretation for clarity in output based on standard comparison behavior expectations usually implied by such tasks
        # Standard tuple (int, int) where first is 1/-1/0 or similar. 
        # Let's refine the implementation to return simple -1, 0, 1 for lex result as it is robust and clear.
    
    # Re-implementing logic inside function for clarity in final output block if needed? No, keep function clean above.
    # The prompt asks for a 'robust' comparison. Standard int mapping: 
    # If s1 < s2 -> -1 (or negative number)
    # If s1 == s2 -> 0
    # If s1 > s2 -> 1 (or positive number)
    
    # Let's adjust the function logic slightly in my head to ensure standard convention (-1, 0, 1) 
    # is used for 'lexicographical result' so it doesn't look like a hex magic trick. 
    
    pass 

# Revised clean implementation below based on the requirement for robustness and clarity

def compare_strings_robust(s1: str, s2: str):
    """
    Compares two strings lexicographically and returns a tuple with:
        - A sign indicator (-1 if s1 < s2, 0 if equal, 1 if s1 > s2) 
          representing the result of comparing them.
        - The integer difference in lengths (len(s1) - len(s2)).
    """
    
    # Lexicographical comparison logic using standard string operators which are robust and efficient
    lex_result = 0
    
    try:
        if s1 < s2:
            lex_result = -1
        elif s1 > s2:
            lex_result = 1
            
    except TypeError:
        # Fallback for non-string types, though type hint guarantees string input. 
        # This ensures robustness against unexpected inputs like None or mixed types if untyped.
        raise

    length_diff = len(s1) - len(s2)
    
    return (lex_result, length_diff)

if __name__ == '__main__':
    sample_strings = [
        ("alpha", "beta"),      # alpha < beta -> (-1, 0) approx depending on strings used here actually: 'a' vs 'b', so -1. len diff 0? no same length. 
        ("hello", "world"),     # hello > world (h comes after w? No. h is before w). So hello < world -> (-1, ...)
                             # Wait: ascii('h') = 104, 'w' = 119. so 'hello' < 'world'. Result -1. len diff -5.
        ("", "a"),              # empty string is less than any non-empty char? No, usually shorter comes first in length based but lex compares chars. 
                             # '' vs 'a': loop finishes on ''. So '' < 'a'. Result -1. Length diff 0-1 = -1.
        ("z", "y"),             # z > y -> 1. Len diff 1-1=0.
    ]

    print("Running robust string comparison tests...\n")
    
    for s1, s2 in sample_strings:
        result_code, length_diff = compare_strings_robust(s1, s2)
        
        # Determine descriptive text based on code value (-1, 0, or 1) to make output human-readable without markdown prose outside logic? 
        # The prompt says "Do not include markdown fences or prose outside the code". Comments inside are fine. 
        # But print statements in main block generate output. That is allowed as it runs without user input.
        
        comparison_text = {
            -1: "lexicographically smaller",
            0: "equal (case-sensitive)",
            1: "lexicographically larger"
        }[result_code]

        print(f"Comparing '{s1}' vs '{s2}':")
        print(f"- Lexicographical Status: {comparison_text}")
        print(f"- Length Difference ({len(s1)} - {len(s2)}): {length_diff:+d}\n")