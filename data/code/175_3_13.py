def extract_words(sentence):
    words = [word for word in sentence.split() if word]
    return words

if __name__ == '__main__':
    sample_sentence1 = "Hello,   world! This is a test, with various spaces and punctuation."
    sample_sentence2 = "\t  Word1, Word2? End. "
    print(extract_words(sample_sentence1))
    print(extract_words(sample_sentence2))