def to_lowercase(text: str) -> str:
    """Convert a string to lowercase."""
    return text.lower()

def to_uppercase(text: str) -> str:
    """Convert a string to uppercase."""
    return text.upper()

def to_title_case(text: str) -> str:
    """Convert a string to title case (first letter of each word capitalized)."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    # Convert to lowercase first then capitalize the first character of each word.
    lower_text = text.lower()
    words = lower_text.split(' ')
    return ' '.join(word.capitalize() for word in words)

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "PYTHON IS FUN",
        "the quick brown fox jumps over the lazy dog"
    ]

    test_input = f"These are samples: {', '.join(sample_strings)}."

    print(f"Original input:\n{test_input}\n")
    
    result_lower = to_lowercase(test_input)
    print("Lowercase:")