import re

class WordMatcher:
    def __init__(self, target_word):
        self.pattern = re.compile(re.escape(target_word), re.IGNORECASE)

    def match_in_list(self, words):
        return [word for word in words if self.pattern.search(word)]

if __name__ == '__main__':
    sample_words = ['Apple', 'banana', 'Cherry', 'apple pie']
    target_word = 'apple'
    matcher = WordMatcher(target_word)
    result = matcher.match_in_list(sample_words)
    print(result)