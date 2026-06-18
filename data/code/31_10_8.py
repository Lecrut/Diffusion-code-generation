def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Time Complexity: O(n) where n is the length of the filtered alphanumeric sequence.
    Space Complexity: O(1) as we modify the list in-place or use two pointers without extra storage beyond input size bounds.
    """
    # Convert to lowercase and filter only alphanumeric characters into a list for efficient access
    cleaned = [c.lower() for c in s if c.isalnum()]

    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True

if __name__ == '__main__':
    # Sample test cases run without user input or external dependencies
    
    sample_strings = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("No 'x' in Nixon", True),
        ("Was it a cat and I saw a badcat?", True),
        ("Hello World!", False),
        ("12321", True),
        ("abcba", True),
        ("abca", False),
    ]

    for test_input, expected in sample_strings:
        result = is_palindrome(test_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] Input: '{test_input}' -> Expected: {expected}, Got: {result}")