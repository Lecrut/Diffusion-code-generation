def remove_all_spaces(text: str) -> str:
    """Remove all spaces from the input string."""
    return ''.join(char for char in text if not (char == ' '))

if __name__ == '__main__':
    sample_input = "Hello World\nThis is a test.\n  Extra   Spaces  \n"
    
    # Simulate reading multi-line string from standard input using the hard-coded value
    result_string = remove_all_spaces(sample_input)
    
    print(result_string)