class SentenceProcessor:
    def __init__(self, sentence):
        self.sentence = sentence

    def get_first_word(self):
        words = self.sentence.split()
        return words[0] if words else ""

if __name__ == '__main__':
    processor = SentenceProcessor("Python is an interpreted, high-level and general-purpose programming language.")
    print(processor.get_first_word())