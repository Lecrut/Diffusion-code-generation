import string

def is_palindrome_two_pointers(s: str) -> bool:
    """
    Checks if a given string is a palindrome using the two-pointer technique.
    
    This implementation ignores case and non-alphanumeric characters, 
    focusing only on letters and digits from both ends of the normalized string.
    
    Time Complexity: O(n), where n is the length of the input string (after normalization).
    Space Complexity: O(1) if using a two-pointer approach without creating new strings,
                       or O(k) if normalizing to lowercase first, where k <= n.

    Args:
        s (str): The input string to check for palindrome property.

    Returns:
        bool: True if the string is a palindrome considering only alphanumeric characters 
              and ignoring case; False otherwise.
    """
    
    # Normalize the string by converting to lowercase and removing non-alphanumeric chars implicitly via pointers logic
    
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        
        if not s[right].isalnum():
            right -= 1
            continue
        
        # Compare characters after converting to lowercase
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon.", True),
        ("Hello World!", False),
        ("madam", True),
        ("hello", False)
    ]

    for input_str, expected_result in test_cases:
        result = is_palindrome_two_pointers(input_str)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"{status}: '{input_str}' -> {result} (Expected: {expected_result})")