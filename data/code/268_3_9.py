class SentenceHandler:
    def __init__(self, sentence):
        self.sentence = sentence
    
    def get_first_word(self):
        words = self.sentence.split()
        return words[0] if words else ''

if __name__ == '__main__':
    handler = SentenceHandler("Hello world from Python")
    print(handler.get_first_word())