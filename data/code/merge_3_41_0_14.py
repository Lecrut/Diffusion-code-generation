def process_string(text: str) -> dict[str, str]:
    """
    Converts a given string to lowercase, uppercase, and title case.

    Args:
        text (str): The input string to be processed.

    Returns:
        dict: A dictionary containing the three transformed strings with keys 
              'lowercase', 'uppercase', and 'title'.
    """
    return {
        "lowercase": text.lower(),
        "uppercase": text.upper(),
        "title": text.title()
    }

if __name__ == '__main__':
    # Hard-coded sample value to ensure the script runs without user input or external dependencies.
    sample_text = "Hello, World! This is a test string."

    result = process_string(sample_text)

    print("Original:", repr(sample_text))
    print("\nLowercase:")
    print(result["lowercase"])
    
    print("\nUppercase:")
    print(result["uppercase"])
    
    print("\nTitle Case:")
    print(result["title"])