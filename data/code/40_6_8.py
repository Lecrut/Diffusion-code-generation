import sys

def get_first_letters(text):
    """
    Extracts the first letter of every word from the given text.
    
    Args:
        text (str): The input string containing words separated by whitespace/newlines.
        
    Returns:
        str: A concatenated string of the first letters, with no spaces or separators between them.
             If a word is empty after stripping, it skips that part.
             Non-alphabetic characters at the start of a 'word' are skipped if they don't form an alphabetic sequence 
             when considering standard tokenization behavior where words are sequences of alphanumeric chars separated by whitespace.
    """
    # Split input into tokens based on any whitespace (spaces, tabs, newlines)
    tokens = text.split()
    
    first_letters = []
    
    for token in tokens:
        if not token:  # Skip empty strings resulting from split behavior with multiple spaces
            continue
            
        # Get the first character of the token and check if it is alphabetic
        char = token[0]
        
        # Only include characters that are letters (a-z, A-Z)
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            first_letters.append(char)
            
    return ''.join(first_letters)

def main():
    """
    Reads text from standard input and prints the result.
    
    Since we cannot use sys.stdin directly in an interactive manner per constraints,
    this function is designed to be called with hardcoded sample data as required by the task instructions.
    In a real production environment where stdin might be piped or redirected, 
    one would typically read from sys.stdin.read(), but strict adherence to "no input()" and avoiding
    implicit interactive prompts means we simulate the reading process via the provided block logic below.
    
    Note: To satisfy 'production-ready' while meeting constraints of no user interaction/syscalls in this specific context,
    we will define a sample variable that represents what would normally come from stdin.
    """
    # Hard-coded sample values as per instructions (no network access or pre-existing files needed)
    sample_input = "Hello World\nThis is Python.\nIt works great!"

    result = get_first_letters(sample_input)
    
    print(result)

if __name__ == '__main__':
    main()