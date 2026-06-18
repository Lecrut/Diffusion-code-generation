import unicodedata

def case_swap(text: str) -> dict[str, str]:
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' 
    to their respective case transformations of the input string.
    
    Prioritizes readability by using Python's built-in methods which are optimized in CPython.
    Performance is maintained as these built-ins are highly efficient for standard ASCII and common Unicode cases.
    Non-alphabetic characters remain unchanged during transformation.

    Args:
        text (str): The input string to transform.

    Returns:
        dict[str, str]: A dictionary with keys 'lower', 'upper', and 'title'.
                        - 'lower': All alphabetic chars converted to lowercase.
                        - 'upper': All alphabetic chars converted to uppercase.
                        - 'title': First char of each word capitalized (others lowercased).
    """
    
    # Lowercase transformation: straightforward built-in method
    lower_text = text.lower()

    # Uppercase transformation: straightforward built-in method
    upper_text = text.upper()

    # Title case transformation: splits by whitespace and capitalizes first char of each word, 
    # then joins them back. This is generally more readable than manual regex iteration for typical use cases.
    words = text.split()
    title_words = [word.capitalize() if len(word) > 0 else "" for word in words]
    title_text = " ".join(title_words)

    return {
        'lower': lower_text,
        'upper': upper_text,
        'title': title_text
    }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    samples = [
        "Hello World",
        "python programming is fun!",
        "123 Main St, Springfield"
    ]

    for text in samples:
        result = case_swap(text)
        print(f"\nInput: '{text}'")
        print("Lower:", f"'{result['lower']}'")
        print("Upper:", f"'{result['upper']}'")
        print("Title:", f"'{result['title']}'")