def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes the first letter of each word in the string while keeping 
    all other letters lowercase, adhering to standard capitalization rules 
    (e.g., 'hello world' becomes 'Hello World').
    
    Args:
        text (str): The input multi-word string.
        
    Returns:
        str: A new string with only the first letter of each word capitalized.
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return text
    
    # Split into words based on whitespace, handling multiple spaces correctly
    parts = text.split()
    
    result_parts = []
    for part in parts:
        if not part:
            continue
        # Capitalize the first character and ensure the rest are lowercase
        capitalized_part = part[0].upper() + part[1:].lower()
        result_parts.append(capitalized_part)
    
    return ' '.join(result_parts)

if __name__ == '__main__':
    sample_inputs = [
        "hello world",
        "python programming is fun!",
        "   multiple    spaces  here ",
        "single word",
        "",
        "UPPERCASE AND lowercase mixed"
    ]

    for test_input in sample_inputs:
        output = capitalize_first_letter_only(test_input)
        print(f'Input: "{test_input}"')
        print(f'Output: "{output}"\n')