import sys

def get_first_letters(text: str) -> list[str]:
    """Extract the first letter of every word from the input text."""
    words = text.split()
    return [word[0] if word else "" for word in words]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, or network access is required.
    sample_text = """Hello World! This is a test script running locally without any prompts."""

    result = get_first_letters(sample_text)
    
    for char in result:
        print(char)