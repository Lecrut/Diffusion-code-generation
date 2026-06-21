def extract_words(sentence):
    return sentence.lower().split()

if __name__ == '__main__':
    sample_sentence = "This is a sample sentence for word extraction and testing."
    words = extract_words(sample_sentence)
    print(words)