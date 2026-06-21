def substring_in_corpus(substring, corpus):
    return substring in corpus

if __name__ == '__main__':
    print(substring_in_corpus("hello", "This is a sample text containing the word hello."))
    print(substring_in_corpus("world", "This is a sample text containing the word hello."))