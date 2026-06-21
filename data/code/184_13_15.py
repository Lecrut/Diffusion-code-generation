def substring_in_corpus(substring, corpus):
    return substring in corpus

if __name__ == '__main__':
    sample_substring = "example"
    sample_corpus = "This is an example sentence for testing."
    print(substring_in_corpus(sample_substring, sample_corpus))