class WordCounter:
    def __init__(self):
        self.word_count = {}

    @staticmethod
    def process_sentence(sentence):
        words = sentence.split()
        return [word.lower() for word in words]

    def count_words(self, sentence):
        words = self.process_sentence(sentence)
        for word in words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1

    def get_word_counts(self):
        return self.word_count

if __name__ == '__main__':
    counter = WordCounter()
    sentence = "Hello world hello"
    counter.count_words(sentence)
    print(counter.get_word_counts())