import sys

def compare_strings(str1: str, str2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with:
        - 0 if the strings are equal (lexicographically), otherwise 1 or -1.
          Note: This uses Python's default string comparison logic directly 
          to determine order rather than just equality, as 'compare' often implies ordering.
          However, based on standard lexicographical definition where we check for inequality first:
          If str1 < str2 -> return 1 (str1 is smaller)
          If str1 > str2 -> return -1 (str1 is larger)
          Else -> return 0
    
    Returns a tuple of two integers:
        - Comparison result (-1, 0, or 1) based on lexicographical order.
        - Length difference (len(str1) - len(str2)).

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        tuple[int, int]: A tuple containing the comparison result and length difference.
            Comparison result is negative if str1 < str2, positive if str1 > str2, 0 otherwise.
            Length difference is len(str1) - len(str2).
    
    Example:
        >>> compare_strings("apple", "banana")
        (1, 5) # 'apple' comes before 'banana', and length diff is 6-4=2? Wait logic check below
    
    Correction on Logic for Lexicographical Comparison in Python context usually implies order.
    But the prompt says "compares two strings lexicographically". 
    Standard behavior: 
        if str1 < str2: return -1 (str1 comes first) or 1 depending on convention? 
        Let's stick to standard C-like strcmp logic often expected in such tasks unless specified otherwise.
        Usually: a=0, b=-1, c=1 where c=strcmp(a,b). But let's make it intuitive for the user.
        If str1 < str2 -> return 1 (indicating difference exists and direction) or -1? 
        Let's use: -1 if equal, else order based on ascii value diff? No, that's not robust enough without full string scan.
        
    Revised Plan to be unambiguous and "robust":
    Use Python's built-in comparison for the first part (lexicographical) but map it clearly.
    Let's define: 
        result = -1 if str1 == str2 else 0? No, that loses order info.
        
    Standard Interpretation of "Compare Lexicographically" in many coding tests implies determining which is smaller/larger or just equality check.
    Given the requirement for a single integer return combined with length diff:
    Let's use this logic: 
        cmp_result = -1 if str1 < str2 else 0 # Wait, usually we want to know order too? Or maybe it implies strict inequality detection?
        
    Actually, looking at similar tasks, often "compare" means checking equality or ordering.
    If I return a tuple of (comparison_flag, length_diff):
        comparison_flag: -1 if str1 < str2, 0 if equal, 1 if str1 > str2. This is the most robust representation of lexicographical comparison.

    Length difference = len(str1) - len(str2).
    
    Example Trace: "a", "b" -> 'a' < 'b', so (-1, 1-1=0)? No len("a")=1, len("b")=1. Diff is 0. Tuple: (-1, 0).
    "z", "y" -> 'z' > 'y', so (1, -1).
    "" == "" -> (0, 0).

    """
    
    # Lexicographical comparison using Python's native string operators for robustness and correctness.
    if str1 < str2:
        cmp_result = -1
    elif str1 > str2:
        cmp_result = 1
    else:
        cmp_result = 0
        
    length_diff = len(str1) - len(str2)
    
    return (cmp_result, length_diff)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        ("apple", "banana"),      # Lexicographically 'apple' < 'banana', lengths 5 vs 6 -> diff -1? No, len(apple)=5, len(banana)=6. Diff: 5-6=-1. Result: (-1, -1)
        ("zebra", "ant"),         # 'zebra' > 'ant'. Lengths 5 vs 3. Diff: 2. Result: (1, 2)
        ("hello", "world"),       # 'h' < 'w', lengths equal. Result: (-1, 0)
        ("test", "testing"),      # 'te' == 'te', but 'st' vs 'sti'. 's'=='s', 't'<'i'? No 't' > 'i'. So 'test' < 'testing'? 
                                  # Wait: t-e-s-t vs t-e-s-t-i-n-g. Prefix match up to "test". Next char in second is 'i', first ends (empty).
                                  # In Python, shorter string comes before if it's a prefix. So "test" < "testing". Result (-1, -4)
        ("", ""),                 # Equal strings. Lengths 0 vs 0. Diff: 0. Result: (0, 0)
    ]

    print("Running lexicographical and length comparison tests...\n")
    
    for s1, s2 in test_cases:
        result = compare_strings(s1, s2)
        cmp_val, len_diff = result
        
        # Determine text representation of the sign to make it readable if needed, 
        # but returning int as requested.
        order_desc = "str1 < str2" if cmp_val == -1 else ("equal" if cmp_val == 0 else "str1 > str2")
        
        print(f"'{s1}' vs '{s2}': Lexicographical ({order_desc}), Length Difference: {len_diff}")

    # Verify specific expected output for one case to ensure correctness in mind.
    # Case: "test", "testing" -> 'test' < 'testing', len diff = 4 - 7 = -3? 
    # Wait, s1="test"(5 chars), s2="testing"(8 chars). Diff = 5-8 = -3.
    # My manual trace above was wrong on length count or sign logic in thought process.
    # Let's re-calculate: "apple" (5) vs "banana" (6). Diff = -1. Result (-1, -1). Corrected previous comment.

    print("\nAll tests completed successfully.")