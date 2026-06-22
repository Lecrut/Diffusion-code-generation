class SentenceAnalyzer:
    def __init__(self, sentence):
        self.sentence = sentence

    def get_longest_word(self):
        words = self.sentence.split()
        longest_word = ""
        max_length = 0
        for word in words:
            if len(word) > max_length:
                longest_word = word
                max_length = len(word)
        return longest_word

if __name__ == '__main__':
    sample_sentence = "A quick brown fox jumps over the lazy dog"
    analyzer = SentenceAnalyzer(sample_sentence)
    print(analyzer.get_longest_word())