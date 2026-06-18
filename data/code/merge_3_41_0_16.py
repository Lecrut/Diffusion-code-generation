def convert_case(text: str) -> dict[str, str]:
    """Converts a string to lowercase, uppercase, and title case."""
    return {
        "lowercase": text.lower(),
        "uppercase": text.upper(),
        "titlecase": text.title()
    }

if __name__ == '__main__':
    sample_text = "Hello World! This is a SAMPLE string."
    
    results = convert_case(sample_text)
    
    print("Original:", repr(sample_text))
    print("\nLowercase:")
    print(results["lowercase"])
    print("\nUppercase:")
    print(results["uppercase"])
    print("\nTitle Case:")
    print(results["titlecase"])