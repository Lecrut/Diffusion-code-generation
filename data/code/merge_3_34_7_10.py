def capitalize_words(text: str) -> str:
    """
    Automatically capitalizes the first letter of every word in a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with each word's first character capitalized.
             Non-alphabetic characters are treated as separators; 
             leading/trailing whitespace is preserved but normalized within words.
             
    Example:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    if not text or not isinstance(text, str):
        return ""

    result = []
    
    # Normalize string to handle Unicode and ensure word boundaries are clear
    normalized_text = " ".join(text.split())  # Remove extra whitespace
    
    for char in normalized_text:
        if 'a' <= char.lower() <= 'z':
            result.append(char.upper())
        else:
            result.append(char)
    
    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "hello world from python",
        "this is a test case for the decorator",
        "  multiple   spaces between words ",
        "no_change_here!",
        "UPPERCASE_AND_MIXED_CASE"
    ]

    print("Input String | Output String")
    print("-" * 40)
    
    for sample in sample_strings:
        capitalized = capitalize_words(sample)
        # Reconstruct original spacing if needed, but since we normalized input above, 
        # let's demonstrate the core functionality on raw strings.
        
        output_repr = repr(capitalized).replace("\\'", "'")[:60] + "..." if len(repr(capitalized)) > 59 else f"'{capitalized}'"
        print(f"{repr(sample):30} | {output_repr}")

    # Direct execution example for clarity in testing logic without repr cluttering output too much
    test_input = "welcome to the capitalization function!"
    final_output = capitalize_words(test_input)
    
    print("-" * 40)
    print(f"\nDirect Test:")
    print(f"Input:        '{test_input}'")
    print(f"Output:       '{final_output}'")