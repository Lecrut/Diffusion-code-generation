class SentenceProcessor:
    def __init__(self, sentence):
        self.sentence = sentence

    def isolate_first_word(self):
        return self.sentence.split()[0]

if __name__ == '__main__':
    processor = SentenceProcessor("Hello world from Python")
    print(processor.isolate_first_word())