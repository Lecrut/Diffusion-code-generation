def process_string(text: str) -> tuple[str, str, str]:
    """Returns a tuple with original string, lowercase version, and reversed case version."""
    lower_text = text.lower()
    
    # Reverse the characters in the lowered text to get 'reversed case'
    reverse_lowered_chars = ''.join(reversed(lower_text))
    
    return (text, lower_text, reverse_lowered_chars)

if __name__ == '__main__':
    sample_input = "Hello World!"
    result = process_string(sample_input)
    print(f"Original: {result[0]}")
    print(f"Lowercase: {result[1]}")
    print(f"Reversed Case: {result[2]}")