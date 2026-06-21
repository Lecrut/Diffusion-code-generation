def validate_sentence(sentence):
    if not isinstance(sentence, str) or not sentence.strip():
        raise ValueError("Invalid input: must be a non-empty string")

def split_sentence(sentence):
    validate_sentence(sentence)
    return sentence.split()

if __name__ == '__main__':
    sample_sentence = "  Hello   world! This is a test sentence. "
    words = split_sentence(sample_sentence)
    print(words)