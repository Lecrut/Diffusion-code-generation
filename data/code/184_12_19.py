import re

class WordSearcher:
    def __init__(self, target_word):
        self.target_pattern = re.compile(re.escape(target_word), re.IGNORECASE)

    def find_in_list(self, words):
        return [word for word in words if self.target_pattern.search(word)]

if __name__ == '__main__':
    searcher = WordSearcher('python')
    sample_words = ['Hello', 'world', 'Python', 'programming']
    result = searcher.find_in_list(sample_words)
    print(result)