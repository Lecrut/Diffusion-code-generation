def calculate_string_length(s: str) -> int:
    """
    Calculate the length of a string, handling both ASCII and Unicode characters efficiently.
    
    In Python 3, strings are unicode by default. The len() function returns the number 
    of code points in the string, which is efficient for most use cases including mixed 
    ASCII/Unicode text. This handles emojis, accented characters, CJK characters correctly.
    
    Args:
        s (str): The input string to measure.
        
    Returns:
        int: The length of the string as a count of code points.
    """
    return len(s)

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    
    test_cases = [
        "Hello, World!",  # Standard ASCII text
        "Café",            # Unicode with accent (café)
        "你好世界",         # Chinese characters
        "🚀✨💡",          # Emojis and special symbols
        "",                # Empty string
        "a" * 10**6,       # Large ASCII string for performance check
    ]

    print("String Length Calculation Results:\n")
    
    for test_str in test_cases:
        length = calculate_string_length(test_str)
        description = f"{test_str[:20]}..." if len(test_str) > 20 else repr(test_str)
        print(f"Input: {description}")
        print(f"Length (code points): {length}\n")