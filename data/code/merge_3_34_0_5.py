import re

def title_case_preserved(s: str) -> str:
    """
    Capitalizes only the first letter of each word in the input string,
    preserving the casing of all subsequent letters within that word.
    
    This function uses a regular expression to find sequences of non-whitespace 
    characters (words). For each match found, it capitalizes the very first 
    character and leaves the rest unchanged if they are already uppercase or
    lowercase as originally provided in the string's specific context for those letters.

    Args:
        s (str): The input string to process.

    Returns:
        str: A new string where only the first letter of each word is capitalized,
             and the rest of the casing from the original word is preserved.
    
    Examples:
        "hello WORLD" -> "Hello WORLD"
        "this Is a TEST case" -> "This Is a Test Case" (Note: logic preserves internal letters)
    """
    if not s or not isinstance(s, str):
        return ""

    # Split the string into words and join them back. 
    # We use regex to match one or more non-whitespace characters as 'words'.
    matches = re.findall(r'\S+', s)
    
    result_parts = []
    
    for word in matches:
        if len(word) > 0:
            first_char = word[0].upper()
            # The rest of the string (from index 1 onwards) is kept exactly as it was.
            remaining_chars = word[1:] 
            result_parts.append(first_char + "".join(remaining_chars))
        else:
            result_parts.append("")

    return " ".join(result_parts)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    samples = [
        "hello world",
        "this Is a TEST case",
        "Python 3.10 is Great!",
        "",
         "   leading and trailing spaces ",
        "multiple    spaces between words"
    ]

    for sample in samples:
        output = title_case_preserved(sample)
        print(f"'{sample}' -> '{output}'")