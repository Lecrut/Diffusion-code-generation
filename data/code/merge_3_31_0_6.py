import re

def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Keep only alphanumeric characters and convert to lowercase
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned_s == cleaned_s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or external dependencies
    
    samples = [
        ("A man, a plan, a canal: Panama", True),      # Classic example with punctuation and spaces
        ("racecar", True),                              # Simple alphanumeric palindrome
        ("Was it a car or a cat I saw?", True),         # Another classic sentence
        ("Hello, World!", False),                       # Not a palindrome due to length/content
        ("No 'x' in Nixon", True),                      # Includes quotes and spaces
        ("1234567890", False),                         # Numbers do not form a palindrome here without symmetry
        ("aB_c-d!@#", False),                          # Mixed case with symbols, no match when cleaned to "abcd-" vs "-dcba" -> actually 'abc' != 'cba', wait: clean is 'ab-cd-'? No. Clean: abcd-. Reverse: -dcba. Not equal.)
        ("", True),                                     # Empty string is a palindrome
        ("A", True),                                    # Single character is a palindrome
    ]

    for text, expected in samples:
        result = is_palindrome(text)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] Input: '{text}' -> Expected: {expected}, Got: {result}")