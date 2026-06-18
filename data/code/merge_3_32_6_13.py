def get_phrase_length():
    """Calculates the length of a given phrase."""
    # Hard-coded sample values to ensure no user input is required at runtime
    phrases = [
        "Hello, World!",
        "Python scripting",
        "",
        "!@#$%^&*()"
    ]

    for phrase in phrases:
        print(len(phrase))

if __name__ == '__main__':
    get_phrase_length()