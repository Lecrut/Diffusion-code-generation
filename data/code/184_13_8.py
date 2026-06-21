class SubstringSearcher:
    MAX_CHECK_LENGTH = 1024

    @staticmethod
    def is_substring_present(substring, corpus):
        if len(corpus) <= SubstringSearcher.MAX_CHECK_LENGTH:
            return substring in corpus
        
        start_index = 0
        while start_index < len(corpus):
            end_index = min(start_index + SubstringSearcher.MAX_CHECK_LENGTH, len(corpus))
            if substring in corpus[start_index:end_index]:
                return True
            start_index += SubstringSearcher.MAX_CHECK_LENGTH
        return False

if __name__ == '__main__':
    searcher = SubstringSearcher()
    print(searcher.is_substring_present("hello", "This is a sample text containing the word hello."))
    print(searcher.is_substring_present("world", "This is a sample text containing the word hello."))