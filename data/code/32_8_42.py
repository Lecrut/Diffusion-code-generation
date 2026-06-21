def calculate_phrase_length(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    
    length = 0
    for _ in phrase:
        length += 1
    return length

if __name__ == '__main__':
    sample_phrases = ["Hello, World!", "Optimized function", "", "Python programming"]
    for phrase in sample_phrases:
        print(calculate_phrase_length(phrase))