def convert_text(text: str) -> dict[str, str]:
    """Converts input text to lowercase, uppercase, and title case."""
    return {
        "lowercase": text.lower(),
        "uppercase": text.upper(),
        "title_case": text.title()
    }

if __name__ == '__main__':
    sample_text = "Hello World! This is a TEST string."
    
    results = convert_text(sample_text)
    
    print(f"Original: {sample_text}")
    print("\nLowercase:")
    print(results["lowercase"])
    print("\nUppercase:")
    print(results["uppercase"])
    print("\nTitle Case:")
    print(results["title_case"])