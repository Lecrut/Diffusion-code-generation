import sys

def get_first_letters(text):
    """Extracts the first letter of every word from the input text."""
    words = text.split()
    return [word[0].lower() if len(word) > 0 else '' for word in words]

if __name__ == '__main__':
    sample_text = "Hello world. This is a test script running without user interaction."
    
    # Process the hard-coded sample text which represents multi-line input logic conceptually
    result_chars = get_first_letters(sample_text)
    
    print("".join(result_chars))