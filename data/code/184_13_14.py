class SubstringSearch:
    @staticmethod
    def find_substring(substring, corpus):
        return substring in corpus

if __name__ == '__main__':
    search_term = "hello"
    full_text = "This is a sample text containing the word hello."
    result = SubstringSearch.find_substring(search_term, full_text)
    print(result)