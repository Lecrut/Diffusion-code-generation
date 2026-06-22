def calculate_phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    return len(phrase)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(calculate_phrase_length(sample_phrase))