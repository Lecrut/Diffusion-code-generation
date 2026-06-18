import string

def remove_all_spaces(s: str) -> str:
    """
    Removes all spaces (internal and external).
    
    Parameters:
        s (str): The input string to process.
        
    Returns:
        str: A new string with no space characters.
    """
    return "".join(c for c in s if not c.isspace())

if __name__ == '__main__':
    # Sample multi-line strings as per task requirements (no external files or input prompts)
    sample_input = "Hello World\nThis is a test.\nAnother line with spaces."

    result_string = remove_all_spaces(sample_input)

    print(result_string)