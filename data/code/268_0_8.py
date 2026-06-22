class SentenceProcessor:
    def __init__(self, sentence):
        self.sentence = sentence

    def extract_first_word(self):
        words = self.sentence.split()
        return words[0] if words else ""

if __name__ == '__main__':
    processor = SentenceProcessor("This is a sample string to test the function")
    first_word = processor.extract_first_word()
    print(first_word)