def substring_in_corpus(substring, corpus):
    if not isinstance(substring, str) or not isinstance(corpus, str):
        raise ValueError("Both substring and corpus must be strings.")
    
    return corpus.find(substring) != -1

if __name__ == '__main__':
    print(substring_in_corpus("hello", "This is a sample text containing the word hello."))
    print(substring_in_corpus("world", "This is a sample text containing the word hello."))