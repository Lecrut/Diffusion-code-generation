import sys

def get_first_letters(text: str) -> list[str]:
    """Extracts the first letter of every word from the input text."""
    words = text.split()
    return [word[0] if word else '' for word in words]

if __name__ == '__main__':
    sample_text = "Hello world\nThis is a test.\nPython scripting is fun!"
    
    # Read all lines from standard input (simulated by the variable above)
    full_input = "\n".join(sample_text.splitlines()) if isinstance(sample_text, str) else ""

    result_letters = get_first_letters(full_input)
    print("".join(result_letters))