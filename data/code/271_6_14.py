class SentenceProcessor:
    def __init__(self, sentence):
        self.sentence = sentence

    def get_longest_word(self):
        words = self.sentence.split()
        longest = ""
        max_length = 0
        for word in words:
            if len(word) > max_length:
                longest = word
                max_length = len(word)
        return longest

if __name__ == '__main__':
    processor = SentenceProcessor("The quick brown fox jumps over the lazy dog")
    print(processor.get_longest_word())