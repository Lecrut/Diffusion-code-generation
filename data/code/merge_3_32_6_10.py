def get_phrase_length():
    """Calculates and prints the length of a phrase."""
    # Hard-coded sample values to run without user input
    phrases = [
        "Hello, World!",
        "Python is great.",
        ""
    ]
    
    for phrase in phrases:
        print(len(phrase))

if __name__ == '__main__':
    get_phrase_length()