import re

def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring case, spaces, 
    punctuation, and other non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_string = re.sub(r'[^a-z0-9]', '', s.lower())
    
    return cleaned_string == cleaned_string[::-1]

def prompt_user():
    """
    Simulates user input by returning a hard-coded sample string directly.
    This adheres to the constraint of not using interactive prompts or sys.stdin.
    """
    # Sample test case: "A man, a plan, a canal: Panama" is a famous palindrome example
    return "A man, a plan, a canal: Panama"

if __name__ == '__main__':
    sample_string = prompt_user()  # Hard-coded sample value as per instructions
    
    result = is_palindrome(sample_string)
    
    if result:
        print(f'The string "{sample_string}" IS a palindrome.')
    else:
        print(f'The string "{sample_string}" is NOT a palindrome.')