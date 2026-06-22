def calculate_phrase_length(phrase):
    return len(phrase)

if __name__ == '__main__':
    sample_phrases = [
        "Hello, World!",
        "Python programming",
        "",
        "  Leading and trailing spaces  ",
        "Special!@#$$%^&*() characters"
    ]
    
    for phrase in sample_phrases:
        print(calculate_phrase_length(phrase))