def convert_text(text: str) -> dict[str, str]:
    """Converts input text to lowercase, uppercase, and title case."""
    return {
        'lowercase': text.lower(),
        'uppercase': text.upper(),
        'title_case': text.title()
    }

if __name__ == '__main__':
    sample_string = "Hello World This Is Python Script"
    
    results = convert_text(sample_string)
    
    print(f"Original: {sample_string}")
    print("-" * 40)
    print("Lowercase:", results['lowercase'])
    print("-" * 40)
    print("Uppercase:", results['uppercase'])
    print("-" * 40)
    print("Title Case:", results['title_case'])