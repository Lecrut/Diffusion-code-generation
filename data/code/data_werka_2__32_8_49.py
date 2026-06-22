def validate_input(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")

def calculate_phrase_length(phrase):
    validate_input(phrase)
    return len(phrase)

if __name__ == '__main__':
    sample_phrases = ["Hello, World!", "Optimized function", "", "Python programming"]
    for phrase in sample_phrases:
        print(calculate_phrase_length(phrase))