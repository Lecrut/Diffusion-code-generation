import re

def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome, ignoring spaces, punctuation, 
    and case sensitivity.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string by keeping only alphanumeric characters and converting to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Compare the normalized string with its reverse
    return cleaned_string == cleaned_string[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "Madam in Eden, I'm Adam",
        "Hello World"
    ]

    print("Testing palindrome detection with the following strings:\n")

    for test_string in sample_strings:
        result = is_palindrome(test_string)
        status = "is a palindrome" if result else "is NOT a palindrome"
        print(f"'{test_string}' {status}")