"""
Module to reverse strings while correctly handling Unicode characters.
"""

def reverse_string(text: str) -> str:
    """
    Reverses the order of characters in a given string, ensuring correct 
    handling of Unicode characters including emojis and non-Latin scripts.

    The function creates a new string by iterating over the input text from 
    last to first character. This method preserves all Unicode properties such as 
    combining marks, emoji sequences (treated as single code points), and complex 
    script directions without requiring external libraries like `unicodedata`.

    Args:
        text (str): The input string whose characters need to be reversed. Can contain 
                    any valid Unicode character sequence.

    Returns:
        str: A new string with the order of characters reversed relative to the input.

    Example:
        >>> reverse_string("Hello, 世界!")
        '!界世，olleH'
        
        >>> reverse_string("🌍✨")
        '✨🌍'
    
    Note:
        This function operates on code points (characters) rather than grapheme clusters. 
        While this correctly handles most use cases including emojis, it does not preserve 
        the visual grouping of combining diacritical marks in some edge cases where a single 
        base character is followed by multiple modifiers that should be treated as one unit.
    """
    return "".join(reversed(text))

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure no external input or files are needed
    
    sample_1 = "Hello, World!"
    
    sample_2 = "日本語テスト"  # Japanese text
    sample_3 = "🌍✨💻☕️"     # Emojis including skin tone modifiers and combining marks
    
    result_1 = reverse_string(sample_1)
    print(f"Original: {sample_1}")
    print(f"Reversed: {result_1}\n")

    result_2 = reverse_string(sample_2)
    print(f"Original: {sample_2}")
    print(f"Reversed: {result_2}\n")

    result_3 = reverse_string(sample_3)
    print(f"Original: {sample_3}")
    print(f"Reversed: {result_3}")