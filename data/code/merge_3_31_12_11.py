def is_palindrome_two_pointer(s: str) -> bool:
    """
    Determines if a string is a palindrome using two pointers.
    Iterates from start to end, comparing characters while ignoring non-alphanumeric ones and case.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Move pointers past non-alphanumeric characters and adjust case for comparison
        while not s[left].isalnum():
            left += 1
        while not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
    
    return True

def is_palindrome_slicing(s: str) -> bool:
    """
    Determines if a string is a palindrome using string slicing.
    Filters for alphanumeric characters and converts to lowercase, then checks equality with reversed slice.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    return filtered == filtered[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test both implementations without user input or external dependencies
    
    samples = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "#a@P#panama!",
        "",
        "Was it a cat and I saw a raccoon?",
        "Madam in Eden, Samed",
        "No 'x' in Nixon"
    ]

    print("Testing Two-Pointer Implementation:")
    for sample in samples:
        result_tp = is_palindrome_two_pointer(sample)
        
    # Print results using list comprehension to avoid printing inside the loop if desired logic change, 
    # but here we iterate and print directly as per standard debugging output.
    for i, sample in enumerate(samples):
        tp_res = is_palindrome_two_pointer(sample)
        sl_res = is_palindrome_slicing(sample)
        
        status_ok = "PASS" if (tp_res == sl_res) else "FAIL"
        print(f"Sample {i+1}: '{sample}' -> TwoPointer: {tp_res}, Slicing: {sl_res} [{status_ok}]")

    # Explicit final check for a known palindrome to ensure correctness at end of run
    test_case = "racecar"
    assert is_palindrome_two_pointer(test_case) == True, "Two pointer failed on simple case"
    assert is_palindrome_slicing(test_case) == True, "Slicing failed on simple case"
    
    print("\nAll assertions passed successfully.")