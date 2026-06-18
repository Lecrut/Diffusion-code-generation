def compare_strings(str1: str, str2: str) -> tuple[int, int]:
    """
    Compares two strings lexicographically and returns a tuple with 
    the comparison result (0 if equal, 1 if first is greater, -1 otherwise)
    and the length difference (length of str1 minus length of str2).

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        tuple[int, int]: A tuple containing:
            - comparison_result (int): 0 if strings are equal lexicographically, 
              1 if str1 > str2, -1 otherwise.
            - length_diff (int): Length of str1 minus length of str2.
    """
    # Lexicographical comparison using standard string operators for robustness and clarity
    cmp_result = 0
    if str1 < str2:
        cmp_result = -1
    elif str1 > str2:
        cmp_result = 1

    length_diff = len(str1) - len(str2)
    
    return (cmp_result, length_diff)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("apple", "banana"),      # Expected: (-1, 5), 'a' < 'b', len(apple)=5, len(banana)=6 -> diff=-1? Wait. 
                                # Correction: len("apple")=5, len("banana")=6. Diff = 5 - 6 = -1.
        ("zebra", "ant"),         # Expected: (1, -3), 'z' > 'a', len(zebra)=5, len(ant)=3 -> diff=2? 
                                # Correction: len("zebra")=5, len("ant")=3. Diff = 5 - 3 = 2.
        ("hello", "world"),       # Expected: (-1, 0), 'h' < 'w', lengths equal (5).
        ("test", "testing"),      # Expected: (-1, -4), 't'=='t', then 'e'<'s'? No. 
                                # Correction: Lexicographically "test" vs "testing". 
                                # t==t, e<in? No, i>e. So "test" < "testing"? Let's trace carefully.
                                # s[0]:'t' == s'[0]'t'. s[1:] 'est' vs 'esting'. 'e' < 'i'? Yes. 
                                # Wait: "test" is prefix of "testing". Usually shorter comes first if equal up to length?
                                # Actually, Python's default comparison stops at the end of the shorter string if they match so far.
                                # If str1 == str2[:len(str1)], then str1 < str2 is True (shorter).
                                # So "test" < "testing". Result -1. Length diff: 4-6 = -2.
        ("", ""),                  # Expected: (0, 0)
    ]

    for i, (s_a, s_b) in enumerate(test_cases):
        result, length_diff = compare_strings(s_a, s_b)
        print(f"Test Case {i + 1}:")
        print(f"String A ({repr(s_a)}), String B ({repr(s_b)})")
        print(f"Lexicographical Comparison: {'A < B' if result == -1 else 'A > B' if result == 1 else 'Equal'} (Result Code: {result})")
        print(f"Length Difference A - B: {length_diff}")
        print("-" * 30)