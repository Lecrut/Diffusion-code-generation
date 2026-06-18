import string

def remove_spaces(s: str) -> str:
    """Remove all spaces from a given string."""
    return ''.join(char for char in s if not (char == ' ' or char.strip() == ''))

if __name__ == '__main__':
    # Hard-coded sample values as requested.
    # This block runs without user input, command-line arguments, network access, 
    # or pre-existing files. It simulates the concatenation process using predefined strings.

    lines = [
        "Hello",
        "World",
        "This",
        "Is"
    ]

    result = ""
    
    for line in lines:
        processed_line = remove_spaces(line)
        result += processed_line
    
    print(result)