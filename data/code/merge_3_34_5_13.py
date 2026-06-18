def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes the first letter of each word in a multi-word string,
    leaving all other letters unchanged (lowercase or mixed).

    This function implements 'title case' logic but strictly adheres to 
    capitalizing only the very first character of every whitespace-separated token.
    
    Args:
        text (str): The input string containing one or more words.
        
    Returns:
        str: A new string with the first letter of each word capitalized,
             and all other letters preserved as they were in the original 
             except for any lowercase following a capital at the start of a word.

    Example:
        >>> capitalize_first_letter_only("hello world")
        'Hello World'
        >>> capitalize_first_letter_only("HELLO WORLD")
        'Helo WOrld'  # Only first letter capitalized per rule interpretation
        """
    if not text or not isinstance(text, str):
        return ""

    words = text.split()
    
    processed_words = []
    for word in words:
        if len(word) > 0:
            # Capitalize only the first character of this specific word
            capitalized_word = word[0].upper() + word[1:]
            processed_words.append(capitalized_word)
        else:
            processed_words.append("")

    return " ".join(processed_words)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        ("hello world", "Hello World"),
        ("HELLO WORLD", "Helo WOrld"),  # Demonstrates strict rule adherence
        ("python programming is fun!", "Python Programming Is Fun!"), 
        (""),                           # Edge case: empty string
        ("   multiple    spaces   ", "Multiple Spaces "),
        ("singleword", "Singleword")
    ]

    print("Testing capitalize_first_letter_only function:")
    for i, (input_str, expected) in enumerate(test_cases):
        result = capitalize_first_letter_only(input_str)
        status = "PASS" if result == expected else f"FAIL (Expected: {expected})"
        print(f"Test Case {i+1}: '{input_str}'")
        print(f"Result: '{result}' - {status}")
        print("-" * 30)