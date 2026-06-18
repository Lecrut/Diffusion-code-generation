def compare_strings_lexicographically(str1: str, str2: str) -> dict:
    """
    Compares two strings lexicographically and returns a detailed comparison object.
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
        
    Returns:
        dict: A dictionary containing the length difference, index of first differing character, 
              and whether one is a prefix of another or they are identical.
    
    Raises:
        TypeError: If either input is not a string.
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")

    length_diff = len(str1) - len(str2)
    
    # Determine the minimum index to check for differences (up to the shorter string's end)
    min_len = min(len(str1), len(str2))
    
    first_difference_index: int | None = None
    
    if str1 == str2:
        return {
            "length_diff": length_diff,
            "first_differing_char_index": -1,  # Indicates strings are identical
            "is_identical": True,
            "str1_prefix_of_str2": False,
            "str2_prefix_of_str1": False
        }

    for i in range(min_len):
        if str1[i] != str2[i]:
            first_difference_index = i
            break
    
    # Determine prefix relationships based on the difference index and lengths
    is_str1_prefix = len(str1) < min_len or (first_difference_index == -1 and len(str1) <= len(str2))
    is_str2_prefix = len(str2) < min_len or (first_difference_index == -1 and len(str2) <= len(str1))

    return {
        "length_diff": length_diff,
        "first_differing_char_index": first_difference_index if first_difference_index != 0 else None, 
        # Note: If index is 0, it means difference at start. Returning -1 for identical handled above.
        # However, to be precise with the prompt asking for 'index of first differing character':
        "first_differing_char_index": first_difference_index if first_difference_index != None else -2, 
        # Using -2 as a sentinel for no difference found within min_len when not identical (shouldn't happen due to str1==str2 check)
        # Re-evaluating logic: If loop finishes without break and strings are not equal, it implies one is prefix of other.
        "is_identical": False,
        "str1_prefix_of_str2": len(str1) <= len(str2), 
        "str2_prefix_of_str1": len(str2) <= len(str1)
    }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_cases = [
        ("apple", "apply"),           # Difference at index 4 ('e' vs 'y')
        ("hello", "world"),          # Difference at index 0 ('h' vs 'w')
        ("test", "testing"),         # str1 is prefix of str2, diff not found in common part
        ("python", "pythons"),       # str2 is prefix of str1? No. str1 longer. Diff at end effectively but handled by length logic mostly here if we consider full string comparison context usually implies checking up to min_len for char mismatch. 
                                      # Actually, let's trace: 'python' vs 'pythons'. Min len 5. Loop runs 0-4. All match. Break not hit. first_difference_index remains None.
        ("abc", "ab"),                # str1 longer than prefix of str2? No, str2 is prefix of str1. Diff effectively at index 3 (end of short).
    ]

    results = []

    for s1, s2 in test_cases:
        comparison_result = compare_strings_lexicographically(s1, s2)
        
        # Formatting the output clearly based on logic derived above
        if "is_identical" not in comparison_result or comparison_result["first_differing_char_index"] == -1:
            print(f"\nComparing '{s1}' and '{s2}':")
            print("- Length Difference:", comparison_result.get("length_diff"))
            
            idx = comparison_result.get("first_differing_char_index", "N/A")
            if isinstance(idx, int) and idx >= 0:
                char_at_idx = s1[idx] if len(s1) > idx else "?"
                print(f"- First differing character index: {idx} (Char in str1: '{char_at_idx}')")
            
            is_identical = comparison_result.get("is_identical", False)
            print("- Strings are identical:", "Yes" if is_identical else "No")
            
            p1_of_p2 = comparison_result.get("str1_prefix_of_str2", False)
            p2_of_p1 = comparison_result.get("str2_prefix_of_str1", False)
            print(f"- '{s1}' is a prefix of '{s2}': {p1_of_p2}")
            print(f"- '{s2}' is a prefix of '{s1}': {p2_of_p1}")

    # Specific trace for "abc" vs "ab": 
    # min_len = 2. Loop i=0 ('a'=='a'), i=1 ('b'=='b'). Loop ends.
    # first_difference_index remains None (initialized as None).
    # is_identical set to False because strings are not equal.
    # str1_prefix_of_str2: len("abc") <= len("ab") -> 3 <= 2 -> False. Correct.
    # str2_prefix_of_str1: len("ab") <= len("abc") -> 2 <= 3 -> True. Correct.
    
    print("\n--- Execution Complete ---\n")