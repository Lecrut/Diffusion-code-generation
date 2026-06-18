import re

def is_palindrome(input_str: str) -> bool:
    """
    Checks if a given string (ignoring spaces, punctuation, and case) 
    reads the same forward and backward.
    
    Parameters:
        input_str (str): The string to check.
        
    Returns:
        bool: True if it is a palindrome, False otherwise.
    """
    # Normalize the string by keeping only alphanumeric characters and converting to lowercase
    normalized = re.sub(r'[^a-z0-9]', '', input_str.lower())
    
    # Compare the cleaned string with its reverse
    return normalized == normalized[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw?",
        "Madam",
        "Hello World"
    ]

    print("--- Palindrome Checker Demo ---\n")

    for s in sample_strings:
        result = is_palindrome(s)
        status = "✓ Is a palindrome" if result else "✗ Not a palindrome"
        print(f'String: "{s}"')
        print(f'Result: {status}\n')