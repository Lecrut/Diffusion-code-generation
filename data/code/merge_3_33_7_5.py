def filter_non_whitespace(s: str):
    """
    Generator function that yields characters from input string 
    excluding whitespace (spaces, tabs, newlines).
    
    Args:
        s (str): Input string to process
        
    Yields:
        char: Single character if not whitespace
    """
    for char in s:
        # Check if the character is a space or any other whitespace using str.isspace()
        if char != ' ':  # Explicitly checking against space as per common interpretation, 
                        # but note that .isspace() covers all whitespace including tabs/newlines
                        # If strict "space" (ASCII 32) was intended: return char if ord(char) != 32 else None
                        pass
        
        # Using isspace to remove ALL types of whitespace as per standard definition
        if not char.isspace():
            yield char

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    test_strings = [
        "Hello World",
        "  Python   ",
        "NoSpacesHere123!",
        "\t\n\tNewlinesAndTabs"
    ]
    
    print("Input -> Output")
    print("-" * 40)
    
    for original in test_strings:
        result = ''.join(filter_non_whitespace(original))
        # Display input and output separated by colon, removing spaces from output visually if needed
        display_result = " ".join(result).replace(' ', '') 
        print(f"{original!r} -> {result}")