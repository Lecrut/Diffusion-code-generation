def convert_string(s: str) -> dict[str, str]:
    """Converts a string to lowercase, uppercase, and title case."""
    return {
        'lowercase': s.lower(),
        'uppercase': s.upper(),
        'title_case': s.title()
    }

if __name__ == '__main__':
    sample_string = "Hello World! This is a Sample String."
    
    results = convert_string(sample_string)
    
    print(f"Original: {sample_string}")
    print("Lowercase:", results['lowercase'])
    print("Uppercase:", results['uppercase'])
    print("Title Case:", results['title_case'])