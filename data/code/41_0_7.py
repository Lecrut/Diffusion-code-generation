def process_string(text: str) -> dict[str, str]:
    """
    Converts a given string into lowercase, uppercase, and title case formats.
    
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
    sample_text = "Hello, World! This is a Sample String."
    
    results = process_string(sample_text)
    
    print("Original:", sample_text)
    print("\nLowercase:")
    print(results["lowercase"])
    print("\nUppercase:")
    print(results["uppercase"])
    print("\nTitle Case:")
    print(results["title"])