class WordIsolator:
    def __init__(self, sentence):
        self.sentence = sentence
    
    def isolate_first_word(self):
        words = self.sentence.split()
        return words[0] if words else ''

if __name__ == '__main__':
    processor = WordIsolator("Hello world from Python")
    print(processor.isolate_first_word())