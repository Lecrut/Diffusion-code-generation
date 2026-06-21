class CaseInsensitiveMatcher:

    def __init__(self, word_list):
        self.word_set = {word.lower() for word in word_list}

    @staticmethod
    def _to_lower(word):
        return word.lower()

    def match(self, word):
        return self._to_lower(word) in self.word_set
if __name__ == '__main__':
    matcher = CaseInsensitiveMatcher(['Java', 'C++', 'python', 'Ruby'])
    print(matcher.match('Python'))
    print(matcher.match('java'))
    print(matcher.match('c++'))
    print(matcher.match('ruby'))
    print(matcher.match('python3'))