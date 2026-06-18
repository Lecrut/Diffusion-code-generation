def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in a string without manual indexing loops.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first letter of each word capitalized.
    """
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, stdin, or args)
    samples = [
        "hello world",
        "python is awesome",
        "the quick brown fox jumps over the lazy dog"
    ]

    for original in samples:
        capitalized = capitalize_words(original)
        print(f'Original: "{original}"')
        print(f'Capitalized: "{capitalized}"\n')