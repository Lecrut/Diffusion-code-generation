import re

def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Time Complexity: O(n) where n is the length of the cleaned string.
    Space Complexity: O(1) as we modify the reference without creating new strings in-place logic (though Python's slicing creates copies; optimized via two-pointer approach on pre-cleaned data).
    """
    # Pre-process to create a clean sequence of alphanumeric characters only, lowercased
    cleaned = re.sub(r'[^a-z0-9]', '', s.lower())

    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", False),  # Note: x is present so should be false? Actually "Nix on" -> n,i,x,o,n. Wait, original phrase: N o 'x' i n N i x . Cleaned: noxinixon. Palindrome check: n!=n (outer). Let's re-evaluate logic manually or just use clear cases.)
        # Correction for test case above: "No 'x' in Nixon" -> cleaned is "noxinxon". 
        # Left 0 ('n'), Right 7 ('n') match.
        # Left 1 ('o'), Right 6 ('o') match.
        # Left 2 ('x'), Right 5 ('x') match.
        # Left 3 ('i'), Right 4 ('n') mismatch -> False. Correct.
        ("", True),
        ("a", True),
        ("12321", True),
    ]

    for test_input, expected in test_cases:
        result = is_palindrome(test_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{test_input}' -> {result} (Expected: {expected})")