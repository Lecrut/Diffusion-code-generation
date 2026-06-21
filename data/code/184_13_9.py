SUBSTRING_THRESHOLD = 10

def find_substring(substring, corpus):
    if len(substring) < SUBSTRING_THRESHOLD:
        return substring in corpus
    else:
        index = corpus.find(substring)
        return index != -1

if __name__ == '__main__':
    print(find_substring("hello", "This is a sample text containing the word hello."))
    print(find_substring("world", "This is a sample text containing the word hello."))