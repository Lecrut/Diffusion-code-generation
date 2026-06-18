import sys

def get_first_letters(text: str) -> list[str]:
    """Extracts the first letter of every word found in the input text."""
    words = text.split()
    return [word[0] if len(word) > 0 else '' for word in words]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, 
    # network access, or pre-existing files are required.
    sample_text = """Hello World!
This is a multi-line test case.
Python makes text processing easy."""

    result = get_first_letters(sample_text)
    
    for letter in result:
        print(letter)