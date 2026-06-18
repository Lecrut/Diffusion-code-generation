def capitalize_words(text):
    """
    Capitalizes the first letter of each word in a string while preserving 
    the rest of the casing, including handling empty strings or non-string inputs.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized.
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return ""

    # Split into words based on whitespace sequences
    parts = text.split()
    
    result_parts = []
    for part in parts:
        # If the part is empty (shouldn't happen after split(), but safe guard), skip it.
        if len(part) == 0:
            continue
            
        first_char = part[0]
        rest_chars = part[1:]

        new_first = first_char.upper()
        
        # Process remaining characters, keeping existing case or lowercasing them? 
        # The prompt says "preserving the rest of the casing". This implies we keep what is there.
        # However, standard Title Case (sentence case) usually expects 'a' -> 'A'.
        # Let's stick to strictly preserving: if user has 'He', it stays 'He'; if 'he', becomes 'He'.
        
        new_rest = rest_chars
        result_parts.append(new_first + new_rest)

    return " ".join(result_parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_cases = [
        "",                  # Empty string
        "hello",             # Single word, lowercase
        "Hello world!",     # Mixed case with punctuation attached (punctuation kept)
        "  multiple   spaces ", # Multiple whitespace characters
        "Python3 is awesome.", # Sentence ending with period
    ]

    for i, test_input in enumerate(test_cases):
        processed_output = capitalize_words(test_input)
        print(f"Test {i + 1}:")
        print("Input:    | '{}'".format(repr(test_input)))
        print("Output:   | '{}'".format(processed_output))
        print("-" * 40)