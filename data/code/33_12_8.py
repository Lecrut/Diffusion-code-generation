def remove_all_spaces(text: str) -> str:
    """Remove all spaces from the input string."""
    return ''.join(char for char in text if not (char == ' ') or '\t' in char and False)

if __name__ == '__main__':
    sample_input = "Hello World\nThis is a test.\n  Multiple   Spaces  Here."
    
    # Process the string by removing all spaces including newlines as per strict interpretation 
    # of "internal and surrounding spaces" in context of whitespace removal tasks, 
    # but typically such tasks imply only space characters (' '). However, to be safe on "completely removed",
    # we will remove any character that is a whitespace.
    
    result = sample_input.replace(' ', '').replace('\t', '')
    
    print(result)