import sys

def get_first_letters(text: str) -> list[str]:
    """Extracts the first letter of every word from the input text."""
    words = text.split()
    return [word[0] if word else '' for word in words if word and not word.startswith('-')]

if __name__ == '__main__':
    sample_text = "Hello world\nThis is a test string.\nPython makes it easy."
    
    # Process the hard-coded sample text to ensure no user input or network access is needed.
    first_letters = get_first_letters(sample_text)
    
    print("".join(first_letters))