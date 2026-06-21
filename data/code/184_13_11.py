def find_substring(substring, corpus):
    return corpus.find(substring) != -1

if __name__ == '__main__':
    search_term = "hello"
    document_text = "This is a sample text containing the word hello."
    result = find_substring(search_term, document_text)
    print(result)