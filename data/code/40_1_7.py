import re

def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list where each element is the first alphabetic character 
                   found at the start of any sequence separated by whitespace or non-alphabetic characters.
                   
    Examples:
        >>> get_first_letters("Hello world")
        ['H', 'w']
        >>> get_first_letters("  Python3 Programming... ")
        ['P', 'P']
    """
    # Use regex to find all words (sequences of alphabetic letters) and extract the first letter from each.
    # \b matches word boundaries, ensuring we capture complete "words" even with mixed separators.
    return [word[0] for word in re.findall(r'\w+', text)]

if __name__ == '__main__':
    sample_strings = ["Hello world", "  Python3 Programming...", "!@# How are you?" , "Single"]
    
    results = []
    for s in sample_strings:
        result = get_first_letters(s)
        results.append(f"Input: '{s}' -> {result}")

    print("\n".join(results))