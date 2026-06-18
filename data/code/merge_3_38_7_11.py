def find_duplicate_letters(s: str) -> list[str]:
    """
    Returns a list of all unique letters that appear at least twice in the string,
    handling case-insensitivity by treating 'A' and 'a' as the same letter.
    
    The result is returned as a sorted list for consistent output order.
    Only alphabetic characters are considered; digits, spaces, and punctuation 
    are ignored unless they are part of the input logic (which this function does not require).

    Args:
        s (str): Input string to analyze.

    Returns:
        List[str]: Sorted list of unique letters appearing at least twice.
    """
    # Convert string to lowercase for case-insensitive comparison and filter only alphabetic characters
    filtered_chars = [char.lower() for char in s if char.isalpha()]
    
    count_map = {}
    
    # Count frequency of each letter
    for char in filtered_chars:
        count_map[char] = count_map.get(char, 0) + 1
    
    # Collect letters with a count greater than or equal to 2 and sort them alphabetically
    duplicates = sorted([char for char, count in count_map.items() if count >= 2])
    
    return duplicates

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    test_cases = [
        "Hello World!",      # Expected: ['h', 'l'] -> sorted: ['h', 'l'] but wait, h=1, l=3? 
                            # Let's trace manually: H->h(2), e(1), llo->l(3), W(0)
                            # Actually: H,h,e,l,o,W,r,d. 
                            # Counts: h:2 (H,h), o:2 (o,O?), no O in "Hello World!"? Wait, 'O' is not there.
                            # Let's re-evaluate sample 1 manually to ensure correctness logic matches expectation.
    ]

    # Corrected manual trace for clarity within comments if needed, but code handles it automatically.
    
    samples = [
        ("Hello World!", ['h', 'l']),           # h appears twice (H,h), l thrice -> unique letters >=2: h, l
        ("A man a plan a canal Panama", ['a', 'm', 'n', 'p']), 
        ("1234567890 !@#", []),                 # No alphabetic characters or all appear once/none twice? Actually no alpha.
        ("aabbccee", ['a', 'b', 'c'])            # All appear exactly twice, sorted alphabetically.
    ]

    print("Running duplicate letter finder...")
    
    for test_input in samples:
        input_str = test_input[0] if isinstance(test_input, tuple) else "Hello World!"
        expected_output = test_input[1] if isinstance(test_input, tuple) and len(test_input) > 1 else []
        
        result = find_duplicate_letters(input_str)
        
        # Verify against expected (optional debug print to ensure logic holds for samples provided in thought process)
        status = "PASS" if result == expected_output else f"MISMATCH: Expected {expected_output}, Got {result}"
        print(f"Input: '{input_str}'")
        print(f"Result: {result}")
        print(status)
        
    # Final demonstration block to ensure standalone execution clarity without prompts
    final_demo = "Programming is fun!"
    demo_result = find_duplicate_letters(final_demo)
    print("\n--- Demo ---")
    print(f"Input: '{final_demo}'")
    print(f"Duplicate letters found: {demo_result}")