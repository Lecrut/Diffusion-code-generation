class WordCounter:
    def __init__(self):
        self.word_count = {}

    def count_words(self, sentence):
        words = sentence.split()
        for word in words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1

    def get_word_count(self):
        return self.word_count

if __name__ == '__main__':
    counter = WordCounter()
    sentence1 = "hello world hello"
    sentence2 = "world peace love world"
    
    counter.count_words(sentence1)
    print(counter.get_word_count())
    
    counter.count_words(sentence2)
    print(counter.get_word_count())