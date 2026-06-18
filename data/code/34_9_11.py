def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized.
             Non-alphabetic characters are preserved as separators; 
             if they appear at the start of a 'word', no capitalization occurs there,
             and standard title casing rules apply based on alphabetic sequences.
    """
    # The most Pythonic approach is to use str.title(), which handles this logic efficiently.
    # It splits by whitespace (and other Unicode separators), checks if the first character 
    # of each segment is an alphabet, capitalizes it, and joins them back together.
    return text.title()

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "this is a test string for pythonic operations",
        "multiple   spaces  between words",
        "mixed CASE: hello WORLD, this IS fine!",
        ""
    ]

    print("Input | Output")
    print("-" * 40)
    
    for s in sample_strings:
        capitalized = capitalize_words(s)
        # Use repr() to show newlines or special characters if any arise from input logic, 
        # though our samples are standard strings.
        result_output = repr(capitalized).replace("''", "'")[:60] + "..." if len(repr(capitalized)) > 58 else repr(capitalized)
        
        print(f"| {repr(s)} | -> {result_output}")

    # Demonstrate the function directly with a clean example
    final_demo = capitalize_words("welcome to the world of python")
    assert "Welcome To The World Of Python" == final_demo, "Functionality check failed."