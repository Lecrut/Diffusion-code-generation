def calculate_phrase_length(text: str) -> int:
    """
    Calculates the length of a given string.
    
    Args:
        text (str): The input string whose length is to be determined.
        
    Returns:
        int: The number of characters in the provided string.

    This function utilizes Python's built-in len() function, which 
    internally uses optimized C implementations for maximum performance and readability.
    
    Example usage with an empty string or Unicode text works seamlessly as intended by default behavior.
    """
    return len(text)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without external input sources
    
    samples = [
        "",                           # Empty string
        "Hello, World!",             # Standard sentence with punctuation and space
        "\u4e0d\u5173\u6bd2",           # Example containing Chinese characters (no harm in Unicode)
        "a" * 1_000_000              # Large string to test efficiency
    ]

    for sample_text in samples:
        phrase_length = calculate_phrase_length(sample_text)
        print(f"Input length: {len(sample_text)}, Calculated length via function: {phrase_length}")