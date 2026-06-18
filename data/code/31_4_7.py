def check_palindrome_with_spaces(s: str) -> bool:
    """
    Verifies if a string is a palindrome, ignoring all spaces, punctuation, 
    and case differences.
    
    Args:
        s (str): The input string to be checked.
        
    Returns:
        bool: True if the cleaned string is a palindrome, False otherwise.
    """
    # Filter out non-alphanumeric characters and convert to lowercase
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    
    # Reverse the list of characters
    reversed_list = filtered_chars[::-1]
    
    # Check if the original cleaned string matches its reverse
    return ''.join(filtered_chars) == ''.join(reversed_list)

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "Not A Palindrome!",
        "Was it a car or a cat I saw?",
        "Hello World"  # Expected to return False
    ]

    for test_case in sample_strings:
        result = check_palindrome_with_spaces(test_case)
        print(f"'{test_case}' is {'a palindrome' if result else 'NOT a palindrome'}")