def transform_string(input_str: str) -> dict[str, str]:
    """
    Converts a given string into lowercase, uppercase, and title case formats.
    
    Args:
        input_str (str): The string to be transformed.
        
    Returns:
        dict: A dictionary containing the three transformed strings with keys 
              'lowercase', 'uppercase', and 'title'.
    """
    return {
        "lowercase": input_str.lower(),
        "uppercase": input_str.upper(),
        "title": input_str.title()
    }

def main():
    # Hard-coded sample values as per requirements. No user interaction or external inputs are used.
    test_string = "Hello, World! This is a Sample string."
    
    results = transform_string(test_string)
    
    print(f"Original: {test_string}")
    print(f"Lowercase: {results['lowercase']}")
    print(f"Uppercase: {results['uppercase']}")
    print(f"Title Case: {results['title']}")

if __name__ == '__main__':
    main()