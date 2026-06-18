import string

def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring case, spaces, 
    punctuation, and other non-alphanumeric characters.
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "race car",
        "Hello World!",
        "Madam",
        "Not a palindrome"
    ]

    print("Running automated palindrome checks with hard-coded samples.\n")

    for test_string in sample_strings:
        result = is_palindrome(test_string)
        status = "IS A PALINDROME" if result else "NOT A PALINDROME"
        print(f'Input: "{test_string}"')
        print(f'Result: {status}\n')

    # Additional manual test case simulation without user input prompt
    manual_test_input = "1234567890"
    result_manual = is_palindrome(manual_test_input)
    print(f'Manual Test Input: "{manual_test_input}"')
    print(f'Result: {"IS A PALINDROME" if result_manual else "NOT A PALINDROME"}\n')

    # Final verification with a known palindrome
    final_check = is_palindrome("Was it a car or a cat I saw?")
    print('Final Verification Input: "Was it a car or a cat I saw?"')
    print(f'Result: {"IS A PALINDROME" if final_check else "NOT A PALINDROME"}\n')

    # Ensure no interactive prompts were triggered by checking return type logic implicitly used above.