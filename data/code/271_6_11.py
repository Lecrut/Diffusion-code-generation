class SentenceAnalyzer:
    def __init__(self, sentence):
        self.sentence = sentence

    def longest_word(self):
        words = self.sentence.split()
        if not words:
            return ""
        longest = words[0]
        for word in words[1:]:
            if len(word) > len(longest):
                longest = word
        return longest

if __name__ == '__main__':
    analyzer = SentenceAnalyzer("The quick brown fox jumps over the lazy dog")
    print(analyzer.longest_word())