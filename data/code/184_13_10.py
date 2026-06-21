def substring_in_corpus(substring, corpus):
    return corpus.find(substring) != -1

if __name__ == '__main__':
    sample_substring = "example"
    sample_corpus = "This is an example text to search for a substring."
    print(substring_in_corpus(sample_substring, sample_corpus))