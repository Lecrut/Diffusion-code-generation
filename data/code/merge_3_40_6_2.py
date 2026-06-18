import sys

def get_first_letters(text: str) -> list[str]:
    """Extracts the first letter of every word from the input text."""
    words = text.split()
    return [word[0] if word else "" for word in words]

if __name__ == '__main__':
    sample_text = "Hello world\nThis is a test case.\nPython scripting is fun!"

    result = get_first_letters(sample_text)
    
    # Print the first letter of each word separated by spaces
    print(" ".join(result))