class WordMatcher:

    def __init__(self, words):
        self.words = [word.lower() for word in words]

    def find(self, target):
        return any((target.lower() == w for w in self.words))
if __name__ == '__main__':
    matcher = WordMatcher(['Python', 'Java', 'C++', 'Ruby'])
    print(matcher.find('python'))
    print(matcher.find('java'))
    print(matcher.find('c++'))
    print(matcher.find('ruby'))
    print(matcher.find('Go'))