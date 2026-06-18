def get_first_letters(strings):
    """
    Takes a list of strings and returns a new list containing 
    just the first letter (character) of each string, handling edge cases like empty strings.
    
    Args:
        strings (list[str]): A list of input strings
        
    Returns:
        list[str]: A list where each element is the first character of the corresponding input string or an empty string if the input was empty
    """
    result = []
    for s in strings:
        # Handle potential None values explicitly, though not expected per task description.
        # If a valid string exists and has content, take its first char. Otherwise append ''.
        if isinstance(s, str) and len(s) > 0:
            result.append(s[0])
        else:
            result.append('')
    return result

def main():
    """
    Main execution block with hard-coded sample values as required by the task constraints.
    No user input or command-line arguments are used here to ensure a standalone, 
    robust run without external dependencies or network access.
    """
    # Hard-coded sample data list of strings for testing purposes
    sample_strings = ["Python", "Robust Scripting", "", "Test String 123"]
    
    first_chars = get_first_letters(sample_strings)

    print("Original Strings and First Letters:")
    for original, char in zip(sample_strings, first_chars):
        print(f"'{original}' -> '{char}'")

if __name__ == '__main__':
    main()