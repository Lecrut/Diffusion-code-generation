MAX_LENGTH = 1024

def extract_first_word(sentence):
    if not isinstance(sentence, str) or len(sentence) > MAX_LENGTH:
        raise ValueError("Input must be a non-empty string up to 1024 characters")
    words = sentence.split()
    return words[0] if words else ""

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    try:
        result = extract_first_word(sample_sentence)
        print(result)
    except ValueError as e:
        print(e)