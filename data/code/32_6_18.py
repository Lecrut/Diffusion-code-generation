import sys

def get_phrase_length():
    """Simulates user input by returning a hard-coded sample phrase."""
    return "Hello, Python!"

if __name__ == '__main__':
    # Simulating the prompt and reading from stdin is avoided as per constraints.
    # We use a hardcoded value to demonstrate functionality without interaction.
    phrase = get_phrase_length()
    
    print(len(phrase))