import unicodedata

def is_palindrome(text: str) -> bool:
    """
    Determines if a string is a palindrome, handling edge cases like 
    empty strings, symbols, and unicode characters (case-insensitive).
    
    Rules applied:
    1. The comparison ignores case differences.
    2. Only alphanumeric characters are considered for the sequence; 
       other symbols/punctuation act as separators/spacers but do not count towards validity.
    3. Empty strings or strings with no valid letters/digits return False (as per robustness requirement).

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the cleaned sequence is a palindrome, else False.
    """
    # Normalize unicode characters and convert to lowercase for comparison
    normalized_text = unicodedata.normalize("NFKD", text).lower()
    
    # Filter out non-alphanumeric characters (keep only letters and digits)
    filtered_chars = [char for char in normalized_text if char.isalnum()]

    # Handle edge case: empty or no alphanumeric content returns False as per prompt requirements
    return len(filtered_chars) > 0 and filtered_chars == list(reversed(filtered_chars))

if __name__ == '__main__':
    # Hard-coded sample values to test robustness without user input
    
    # Test cases covering various scenarios including symbols, unicode, and mixed content
    samples = [
        "A man a plan a canal Panama",  # Standard palindrome with spaces/symbols
        "",                             # Empty string (expected: False)
        "!@#$%",                        # Only symbols (expected: False)
        "12345",                       # No reverse match (expected: False)
        "12321",                        # Numeric palindrome (expected: True)
        "No 'x' in Nixon!",             # Mixed case and punctuation (expected: True)
        "上海自来水来自海上",           # Chinese characters palindrome (expected: True)
        "Able was I ere I saw a Bale"   # Classic sentence with irregular spacing/symbols (expected: False due to extra spaces? Actually standard test is 'A man...') -> Standard version usually works if normalized correctly. Let's stick to simple ones for this specific implementation logic which removes non-alnum.
    ]

    print("Running Palindrome Checker Tests...\n")
    
    # Execute tests and display results directly without interactive prompts
    for i, test_str in enumerate(samples):
        result = is_palindrome(test_str)
        status = "PASS" if result else "FAIL"  # Note: For 'A man a plan...', our logic filters symbols/spaces leaving 'amanaplanacanalpanama', which IS a palindrome. 
                                                # The sample "!@#$%" correctly fails because list becomes empty -> False.
        
        print(f"Test {i+1}: Input='{test_str}'")
        print(f"Result: {'Palindrome' if result else 'Not Palindrome'} (Status: {status})\n")

    # Explicit verification of the specific edge cases mentioned in task description
    empty_check = is_palindrome("")
    symbol_only_check = is_palindrome("!!!@@@##")
    
    print(f"Empty string check (''): {'PASS' if not empty_check else 'FAIL'} (Expected: False)")
    print(f"Symbol-only string check ('!!!@@@##'): {'PASS' if not symbol_only_check else 'FAIL'} (Expected: False)")