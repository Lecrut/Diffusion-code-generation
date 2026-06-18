def process_string(text: str) -> tuple[str, str, str]:
    """
    Returns a tuple with the original string, its lowercase version, 
    and its reversed case version (characters swapped between upper/lower).
    
    Args:
        text (str): The input string.
        
    Returns:
        tuple[str, str, str]: A tuple containing (original_text, lower_case_text, reverse_case_text)
    """
    original = text
    lower_version = text.lower()
    
    # Create a mapping for case reversal logic based on the character's lowercase form
    reversed_chars = []
    for char in text:
        if 'a' <= char <= 'z':
            reversed_char = chr(ord('A') + ord(char) - ord('a'))
        elif 'A' <= char <= 'Z':
            reversed_char = chr(ord('a') + ord(char) - ord('A'))
        else:
            # Non-alphabetic characters remain unchanged in case reversal logic as per standard interpretation
            reversed_char = char
        
        reversed_chars.append(reversed_char)
    
    reverse_case_version = ''.join(reversed_chars)

    return original, lower_version, reverse_case_version

if __name__ == '__main__':
    sample_input = "Hello World!"
    result_tuple = process_string(sample_input)
    print(f"Original: {result_tuple[0]}")
    print(f"Lowercase: {result_tuple[1]}")
    print(f"Reversed Case: {result_tuple[2]}")