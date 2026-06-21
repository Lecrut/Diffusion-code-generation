class SentenceProcessor:
    def __init__(self, sentence):
        self.sentence = sentence

    def split_and_reverse(self):
        words = self.sentence.split()
        reversed_words = words[::-1]
        return reversed_words

if __name__ == '__main__':
    processor = SentenceProcessor("this is a test string")
    result = processor.split_and_reverse()
    print(result)