def convert_string(text: str) -> dict[str, str]:
    """Converts a given string to lowercase, uppercase, and title case."""
    return {
        'lowercase': text.lower(),
        'uppercase': text.upper(),
        'title_case': text.title()
    }

if __name__ == '__main__':
    sample_text = "Hello World This Is A Test String"
    
    result = convert_string(sample_text)
    
    print("Original:", repr(sample_text))
    print("\nLowercase:")
    print(result['lowercase'])
    print("\nUppercase:")
    print(result['uppercase'])
    print("\nTitle Case:")
    print(result['title_case'])