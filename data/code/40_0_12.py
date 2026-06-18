import re

def get_first_letters(text: str) -> list[str]:
    """
    Extracts the first letter of each word from the input string.
    
    Handles various whitespace scenarios including multiple spaces, tabs, newlines,
    and leading/trailing whitespaces efficiently using regular expressions.
    
    Args:
        text (str): The input string containing words separated by whitespace.
        
    Returns:
        list[str]: A list of single-character strings representing the first letter 
                   of each word found in the input. If no words are present, returns an empty list.
    """
    # Split the text into tokens based on any sequence of whitespace characters.
    # This automatically handles multiple spaces, tabs, newlines, etc., and ignores leading/trailing whitespace.
    tokens = re.split(r'\s+', text)
    
    result = []
    for token in tokens:
        if len(token) > 0:
            first_char = token[0]
            
            # Ensure the character is alphabetic to avoid including digits or symbols as "letters"
            # If strict letter-only requirement isn't specified, we could just take any char. 
            # Based on standard interpretation of "letter", we check for alphanumeric (a-z, A-Z).
            if first_char.isalpha():
                result.append(first_char)
    
    return result

if __name__ == '__main__':
    sample_inputs = [
        "Hello World!",
        "  Python   Programming ",
        "\tNew\nLine\tTest",
        "",
        "No words here, just spaces.",
        "A1 B2 C3" # Testing with numbers to see if they are filtered out based on isalpha() check above. 
                 # If the requirement implies any non-whitespace character starts a word:
    ]

    for sample in sample_inputs:
        output = get_first_letters(sample)
        print(f'Input: "{sample}"')
        print(f'Output: {output}')
        print("-" * 20)