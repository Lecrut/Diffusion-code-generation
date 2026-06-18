def is_palindrome(text):
    """Check if a string (ignoring spaces) reads the same forwards and backwards."""
    clean_text = ''.join(char.lower() for char in text if not ' '.isspace(char))
    return clean_text == clean_text[::-1]

if __name__ == '__main__':
    # Sample values to test without user input
    sample_inputs = [racecar, "A man a plan a canal Panama", 23605430652]

    for val in sample_inputs:
        result = is_palindrome(val)
        print(f"Input: '{val}'")
        if isinstance(result, bool):
            status = "IS A palindrome" if result else "NOT a palindrome"