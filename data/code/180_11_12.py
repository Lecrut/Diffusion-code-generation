def find_word_in_corpus(target_word, corpus):
    words_set = set(corpus.split())
    return target_word in words_set

if __name__ == '__main__':
    sample_corpus = "This is a sample corpus. It contains multiple sentences and words."
    target_word = "sample"
    print(find_word_in_corpus(target_word, sample_corpus))