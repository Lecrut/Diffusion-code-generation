class CaseInsensitiveMatcher:

    def __init__(self, word_list):
        self.word_list = [word.lower() for word in word_list]

    def match(self, word):
        return any((w == word.lower() for w in self.word_list))
if __name__ == '__main__':
    matcher = CaseInsensitiveMatcher(['Java', 'C++', 'python', 'Ruby'])
    print(matcher.match('Python'))
    print(matcher.match('java'))
    print(matcher.match('c++'))
    print(matcher.match('ruby'))
    print(matcher.match('python3'))