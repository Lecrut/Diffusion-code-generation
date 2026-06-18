def check_palindrome_with_spaces(text: str) -> bool:
    """
    Verifies if a string is a palindrome, ignoring all spaces and punctuation, 
    and being case-insensitive.
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome under the specified rules, False otherwise.
    """
    cleaned_text = ''.join(
        char.lower() 
        for char in text 
        if not char.strip().isspace() and not any(c.isalnum())  # Filter based on alphanumeric check later
    
    )
    
    # Re-approach cleaning: keep only alphanumeric characters, convert to lowercase
    filtered_chars = [c for c in text]
    cleaned_text = ''.join([char.lower() if char.isalpha() or char.isdigit() else '' 
                            for char in filtered_chars])

    return cleaned_text == reversed(cleaned_text)

if __name__ == '__main__':
    sample_inputs = {
        "A man, a plan: a canal: Panama", True,
        "Was it a car or a cat I saw?", True,
        "Hello World!", False,
        "racecar", True,
        "" ,True  # Empty string is technically a palindrome
    }

    test_cases = [item for item in sample_inputs.items() if len(item) == 2]
    
    results = {}
    for input_str, expected_result in (sample_inputs.items()):
        actual_result = check_palindrome_with_spaces(input_str)
        results[input_str[:30] + "..." if len(input_str) > 30 else input_str] = {
            "input": repr(input_str), 
            "expected": str(expected_result).lower(), 
            "actual": str(actual_result).lower()
        }