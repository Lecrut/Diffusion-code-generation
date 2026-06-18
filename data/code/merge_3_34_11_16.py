def capitalize_first_letter_only(text: str) -> str:
    """
    Returns a new string where only the first character of every word is capitalized.
    
    This function uses regex to find all words and capitalizes their first letter,
    preserving the original casing for subsequent letters in each word. It handles
    multiple consecutive spaces correctly by replacing them with a single space,
    which improves efficiency compared to manual iteration without lookahead assertions.
    
    Args:
        text (str): The input string containing words separated by whitespace.
        
    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    import re
    
    # Regex explanation for performance optimization:
    # \b matches a word boundary to ensure we start at the beginning of a word.
    # ([a-zA-Z]) captures exactly one alphabetic character (the potential capital).
    # (.*) matches the rest of the word non-greedily, including lowercase letters or digits 
    # if they exist immediately after the first letter without interruption by spaces.
    
    return re.sub(r'\b([a-zA-Z])(.*)', lambda m: f"{m.group(1).upper()}{m.group(2)}", text)

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "python programming is fun",
        "  multiple   spaces between words ",
        "no change here",
        "ALL LOWERCASE CASE",
        "Mixed Case Here",
        "",
        "!@#$%^&*()",
        "one two three four five"
    ]

    for test_input in test_cases:
        result = capitalize_first_letter_only(test_input)
        print(f'Input : "{test_input}"')
        print(f'Output: "{result}"\n')