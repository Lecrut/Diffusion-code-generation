def convert_string(text: str) -> dict[str, str]:
    """Converts a given string to lowercase, uppercase, and title case."""
    return {
        "lowercase": text.lower(),
        "uppercase": text.upper(),
        "title_case": text.title()
    }

if __name__ == '__main__':
    sample_text = "Hello World! This is a TEST string."
    
    results = convert_string(sample_text)
    
    print(f"Original: {sample_text}")
    print(f"\nLowercase: {results['lowercase']}")
    print(f"\nUppercase: {results['uppercase']}")
    print(f"\nTitle Case: {results['title_case']}")