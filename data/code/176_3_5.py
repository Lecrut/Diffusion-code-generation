def split_sentence(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    return sentence.split()

if __name__ == '__main__':
    sample_text = "This is a sample sentence for word extraction and testing."
    words = split_sentence(sample_text)
    print(words)